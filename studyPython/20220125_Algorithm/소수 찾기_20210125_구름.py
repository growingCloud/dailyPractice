# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

# def isPrime(num) :
#     for i in range(2, num) :
#         if num % i == 0 :
#             return False
#     return True
#
# def solution(n):
#     count = 0
#     for i in range(2, n + 1) :
#         if isPrime(i) == True:
#             count += 1
#     return count
#
# print(solution(10))
# print(solution(5))


def solution(n):
    # 에라토스테네스의 채 초기화 n 개의 요소에 True 설정 (소수로 간주)
    sieve = [True] * (n + 1)
    # n의 최대 약수가 sqrt(n) 이하 이므로 i = sqrt(n) 까지 검사

    m = int((n + 1) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, (n + 1), i):  # i 이후, i 의 배수를 False 판정
                sieve[j] = False

    return len([i for i in range(2, (n + 1)) if sieve[i] == True]) # 소수 목록

print(solution(10))
print(solution(5))