# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# n은 0 이상 3000이하인 정수입니다.

def solution(n):
    li = []

    for i in range (1, n + 1):
        if n % i == 0 :
            li.append(i)

    answer = sum(li)
    return answer


# -------------------------------- [이선생님 어시스트]

solution = lambda x:sum([i for i in range(1, x//2+1) if not x % i] + [x])