from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, abort, redirect, url_for
# abort : 입력이 잘못 되었을때 오류 페이지를 내보내기 위한 모듈
from datetime import datetime
from bson.objectid import ObjectId  # {'_id': ObjectId(idx)}에서 idx를 ObjectId의 형태로 받기 위한 모듈
import time

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbpractice


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('write.html')


# current_time(datetime)을 우리가 보는 시간으로 바꿔주는 함수
# 이렇게 번거로운 과정을 거치는 이유? -> (내 생각) mongo에는 가공하기 쉽게 밀리초 단위의 시간으로 저장해뒀다가 꺼낼때 우리가 보는 시간으로 바꿔주기 위해!
@app.template_filter('format_datetime')
def format_datetime(value) :
    if value is None :
        return ''   # 만약 시간값이 없다면 공백을 반환

    now_timestamp = time.time()     # offset = utc time과 한국의 time 시차 (+9:00)
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    value = datetime.fromtimestamp((int(value) / 1000)) + offset
    return value.strftime('%Y-%m-%d %H:%M:%S')


# 게시글 작성 (Create)
@app.route('/write', methods=['GET', 'POST'])
def board_write():
    if request.method == "POST" :
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
        return redirect(url_for("board_view", idx=idx.inserted_id))

    else :
        # /write 경로로 들어오면 GET으로 받아 입력창 보여줌
        return render_template('write.html')


# 게시글 상세 페이지 (Read)
@app.route('/view', methods=['GET'])
def board_view():
    idx = request.args.get("idx")
    if idx is not None :
        data = db.board.find_one({'_id': ObjectId(idx)})

        if data is not None :
            view_data = {
                # 'id': data.get('_id'), >> bson 타입이라 제외함 (objectid is not json serializable)
                'name': data.get('name'),
                'title': data.get('title'),
                'contents': data.get('contents'),
                'pubdate': data.get('pubdate'),
                'view': data.get('view')
            }

            return jsonify({'result': 'success', 'view_datas': view_data})
    return abort(404)   # 맞는 페이지가 없을때 404 페이지 내보내기

if __name__ == '__main__':
    app.run('0.0.0.0', port=5005, debug=True)