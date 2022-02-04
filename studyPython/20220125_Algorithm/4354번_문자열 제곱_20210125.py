# 알파벳 소문자로 이루어진 두 문자열 a와 b가 주어졌을 때, a*b는 두 문자열을 이어붙이는 것을 뜻한다.
# 예를 들어, a="abc", b="def"일 때, a*b="abcdef"이다.
# 이러한 이어 붙이는 것을 곱셈으로 생각한다면, 음이 아닌 정수의 제곱도 정의할 수 있다.

# a^0 = "" (빈 문자열)
# a^(n+1) = a*(a^n)
# 문자열 s가 주어졌을 때, 어떤 문자열 a에 대해서
# s=a^n을 만족하는 가장 큰 n을 찾는 프로그램을 작성하시오.

import sys


while True:
    input_str = sys.stdin.readline().strip()
    if input_str == ".":
        break
    for i in range(1, len(input_str) + 1):
        if len(input_str) % i != 0:
            continue
        cut = input_str[0:i]
        if cut[-1] != input_str[-1]:
            continue
        if cut * (len(input_str)//i) == input_str:
            print(len(input_str)//i)
            break


