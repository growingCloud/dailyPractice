# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.

def solution(s):
    # 처음부터 바로 함수에는 구현하기 어려우니까 일단 입력 문자를 가지고 와봄
    # 그리고 이걸 아스키 코드 형태로 바꿔줘야 하니까 일단 리스트 형태로 받아봐야지

    li = list(s)
    # 그리고 리스트로 잘 받아왔는지 확인하기 위해서 프린트 한번 해보기
    print(li)
    # 잘 들어오는거 확인 했음!
    # 이제 포문으로 하나씩 숫자로 바꿔보자

    numbering_li = []
    # 숫자로 바꾼거 넣어줄 빈 리스트 하나 만들어 놓기

    for i in li:
        alpha = ord(i)
        # 잘 바뀌는지 확인하기 위해서 프린트 한번 해보기
        # print(alpha)
        numbering_li.append((alpha))
        # print(numbering_li)

    # 숫자로 바꾼 리스트를 큰 순서대로 내림차순 정렬 해주기
    numbering_li.sort(reverse=True)

    string_li = []
    # 문자로 바꾼거 넣어줄 빈 리스트 하나 만들어 놓기

    for j in numbering_li:
        beta = chr(j)
        # 잘 바뀌는지 확인하기 위해서 프린트 한번 해보기
        # print(beta)
        string_li.append(beta)
        # print(string_li)

    # 마지막으로 리스트를 다시 문자열로 합쳐주기

    answer = ''.join(string_li)

    return answer