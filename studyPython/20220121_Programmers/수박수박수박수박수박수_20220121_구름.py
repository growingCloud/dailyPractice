# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# n은 길이 10,000이하인 자연수입니다.


def solution(n):
    li = []

    for i in range(n):
        if i % 2 == 1:
            li.append("박")
        else:
            li.append("수")

    answer = "".join(li)
    return answer


# ------------------- [이선생님 어이스트]


def solution(n):
    water_melon = ""

    for i in range(n):
        if i % 2 == 1:
            water_melon += "박"
        else:
            water_melon += "수"

    return water_melon