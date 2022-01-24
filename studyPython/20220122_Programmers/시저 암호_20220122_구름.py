# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
# 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다.
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

s1 = "AB"       # result = 	"BC"
s2 = "z"        # result = 	"a"
s3 = "a B z"    # result = 	"e F d"
n1, n2, n3 = 1, 1, 4

# ord(문자), cha(숫자) : 아스키 코드 활용

# 문자열을 리스트로 받으면서 아스키코드 숫자로 바꿔서 리스트에 집어넣어줌
# 구한 아스키 코드 숫자값에 n 값을 더해서 새 리스트에 넣어주기
# 새 리스트의 숫자들을 다시 문자로 바꿔서 넣어줘야 함
# 공백은 어떻게 처리 할 것인가? (공백은 32)

list(s3)
li = []
ascii = []

for i in s3: li.append(i)
for i in li: ascii.append(ord(i))


print(li)
print(ascii)