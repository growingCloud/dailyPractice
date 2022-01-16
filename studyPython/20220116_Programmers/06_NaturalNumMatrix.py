# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# n은 10,000,000,000이하인 자연수입니다.

def solution(n):
    n = list(str(n))

    answer = []

    for i in range(len(n)):
        a = len(n) - i - 1
        answer.append(int(n[a]))

    return answer