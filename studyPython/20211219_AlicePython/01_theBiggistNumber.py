# 01. 가장 큰 자릿수 숫자 구하기
# 사용자로부터 자연수를 입력받고 가장 큰 자릿수의 숫자를 출력하세요.
# 입출력 예시 : (753 -> 7), (10999 -> 1)


num = input()

position = 10 ** (len(num)-1)
max = int(num) // position

print(max)


