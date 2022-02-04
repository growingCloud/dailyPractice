def solution(n):
    n = list(str(n))

    answer = []

    for i in range(len(n)):
        a = len(n) - i - 1
        answer.append(int(n[a]))

    return answer