from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, abort, redirect, url_for, session
# abort : 입력이 잘못 되었을때 오류 페이지를 내보내기 위한 모듈
from datetime import datetime, timedelta
from bson.objectid import ObjectId  # {'_id': ObjectId(idx)}에서 idx를 ObjectId의 형태로 받기 위한 모듈
import time
import math

app = Flask(__name__)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)    # 로그인 세션 유지시간
client = MongoClient('localhost', 27017)
db = client.dbpractice


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('login.html')


# current_time(datetime)을 우리가 보는 시간으로 바꿔주는 함수
# 이렇게 번거로운 과정을 거치는 이유? -> (내 생각) mongo에는 가공하기 쉽게 밀리초 단위의 시간으로 저장해뒀다가 꺼낼때 우리가 보는 시간으로 바꿔주기 위해!
@app.template_filter('format_datetime')
def format_datetime(value):
    if value is None:
        return ''  # 만약 시간값이 없다면 공백을 반환

    now_timestamp = time.time()  # offset = utc time과 한국의 time 시차 (+9:00)
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    value = datetime.fromtimestamp((int(value) / 1000)) + offset
    return value.strftime('%Y-%m-%d %H:%M:%S')


# 게시글 작성 (Create)
@app.route('/write', methods=['GET', 'POST'])
def board_write():
    if request.method == "POST":
        # 내용이 입력되어 있는 상태에서는 POST로 받음
        name_receive = request.form['name_give']
        title_receive = request.form['title_give']
        contents_receive = request.form['contents_give']

        # UTC 타임으로 시간 받아와서 서버에 저장
        # 시간을 받아오는 함수 utcnow()
        # 가공하기 편한 상태로 받아오기 위한 함수 timestamp()
        current_time = round(datetime.utcnow().timestamp() * 1000)

        posting = {
            'name': name_receive,
            'title': title_receive,
            'contents': contents_receive,
            'pubdate': format_datetime(current_time),
            'view': 0
        }
        # db.board.insert_one(posting)

        # SQL의 primary key와 같은 고유 번호(_id) 출력
        idx = db.board.insert_one(posting)
        # print(idx.inserted_id)
        # return redirect(url_for("board_view", idx=idx.inserted_id))
        return redirect(url_for('board_view', idx=idx.inserted_id))

    else:
        # /write 경로로 들어오면 GET으로 받아 입력창 보여줌
        return render_template('write.html')


# 게시글 상세 페이지 (Read) ★★★★★★★★★★★★★★★★
@app.route('/view', methods=['GET'])
def board_view():
    idx = request.args.get("idx")
    if idx is not None:
        data = db.board.find_one({'_id': ObjectId(idx)})

        if data is not None:
            view_data = {
                # 'id': data.get('_id'), >> bson 타입이라 제외함 (objectid is not json serializable)
                'primary': str('_id'),
                'name': data.get('name'),
                'title': data.get('title'),
                'contents': data.get('contents'),
                'pubdate': data.get('pubdate'),
                'view': data.get('view')
            }
            return render_template('view.html', result = view_data)
    return abort(404)  # 맞는 페이지가 없을때 404 페이지 내보내기


# 게시글 리스트 페이지 (Read_List) ★★★★★★★★★★★★★★★★
@app.route('/list', methods=['GET'])
def board_lists():
# 페이지 기능 구현 (1)
    # 페이지 값, 값이 없는 경우 기본값은 1
    page = request.args.get("page", 1, type=int)
    # 페이지 당 게시물 출력 갯수 (현재 10개로 설정)
    limit = request.args.get("limit", 10, type=int)

# 검색 기능 구현
    search = request.args.get("search", -1, type=int)
    keyword = request.args.get("keyword", type=str)

    query = {}      # 최종적으로 완성된 쿼리를 만들 변수
    search_list = []

    # 게시글 검색 기능의 option value (0, 1, 2, 3)
    if search == 0:
        search_list.append({"title": {"$regex": keyword}})           # '안녕하세요' 중에서 '녕'자를 찾아주는 기능 (중간 검색)
    elif search == 1:
        search_list.append({"contents": {"$regex": keyword}})
    elif search == 2:
        search_list.append({"title": {"$regex": keyword}})
        search_list.append({"contents": {"$regex": keyword}})
    elif search == 3:
        search_list.append({"name": {"$regex": keyword}})

    # 검색 대상이 하나라도 존재 할 경우, query 변수에 $or 리스트를 쿼리한다 (다중검색을 위한 기능)
    if len(search_list) > 0 :
        query = {"$or" : search_list}
    print(query)

# 페이지 기능 구현 (2)
    lists = list(db.board.find({}, {'_id': False})
                 .skip((page - 1) * limit).limit(limit))

    # 페이지네이션 구현 (라이브러리 사용X)
    # total_count = db.board.find({query}).count()                 # 게시물의 총 갯수
    # last_page_num = math.ceil(total_count / limit)          # 마지막 페이지의 수, 게시물이 하나라도 있으면 페이지가 존재해야 하므로 소수점이 생기면 무조건 올림!
    # block_size = 5                                          # 페이지 블럭을 5개씩 지정
    # block_num = int((page - 1) / block_size)                # 현재 게시글 블럭의 위치
    # block_start = int((block_size * block_num) + 1)         # 블럭의 시작 위치
    # block_end = math.ceil((block_start + block_size - 1))   # 블럭의 끝 위치
    # search = search
    # keyword = keyword

    # page_nation = (page, limit, total_count, last_page_num, block_size,
    #                block_num, block_start, block_end, search, keyword)

    # return jsonify({'postings': lists, 'making-pages': page_nation})
    return render_template('list.html', result = lists)


# 회원가입 페이지 (Join)
@app.route('/join', methods=['GET', 'POST'])
def member_join():
    if request.method == "POST" :
        name_receive = request.form['name_give']
        email_receive = request.form['email_give']
        pw_receive = request.form['pw_give']
        pw_check_receive = request.form['pw_check_give']

        # 가입 시 빈칸이 있을 경우
        # if name_receive is None or email_receive is None or pw_receive is None or pw_check_receive :
        #    return render_template('join.html')

        # 비밀번호 확인과 일치하지 않을 경우
        # if pw_receive != pw_check_receive:
        #    return render_template('join.html')

        # 이메일(아이디) 중복 검사사
        # count = db.members.find({"email" : email_receive}).count()
        # if count > 0:
        #    return render_template('join.html')

        current_time = round(datetime.utcnow().timestamp() * 1000)

        member_join = {
            'name': name_receive,
            'email': email_receive,
            'pw': pw_receive,
            'joindate': current_time,
            'logintime': "",
            'logincount': 0
        }
        db.members.insert_one(member_join)
        return ""

    else:
        return render_template('join.html')


# 로그인 페이지 (Login)
@app.route('/login', methods=['GET', 'POST'])
def member_login():
    if request.method == "POST" :
        email_receive = request.form['email_give']
        pw_receive = request.form['pw_give']
        current_time = round(datetime.utcnow().timestamp() * 1000)

        id_info = db.members.find_one({"email": email_receive})

        if id_info is None:
            return render_template('login.html')
        else:
            if id_info.get('pw') != pw_receive :
                session["id"] = email_receive
                session["name"] = id_info.get('name')
                session["idx"] = str(id_info.get('_id'))
                session.permanent = True
                return redirect(url_for(""))
            else:
                return render_template('list.html')

        return ""

    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)
