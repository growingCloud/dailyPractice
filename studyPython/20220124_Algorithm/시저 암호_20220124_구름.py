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
s4 = "kl"
s5 = "Z"
n1, n2, n3, n4 = 1, 1, 4, 15

# ord(문자), chr(숫자) : 아스키 코드 활용

# 문자열을 리스트로 받으면서 아스키코드 숫자로 바꿔서 리스트에 집어넣어줌
# 구한 아스키 코드 숫자값에 n 값을 더해서 새 리스트에 넣어주기
# 새 리스트의 숫자들을 다시 문자로 바꿔서 넣어줘야 함
# 공백은 어떻게 처리 할 것인가? (공백은 32)

def solution(s, n):
    li = []
    ascii1 = []
    ascii2 = []


    for i in s: li.append(i)
    for i in li: ascii1.append(ord(i))

    for j in ascii1:
        if j != 32:
            if ord("A") <= j <= ord("Z"):
                j = j + n
                if ord("Z") < j:
                    print("0-1 :", j)
                    j = j - 26
                    print("0-2 :", j)
                j = chr(j)
                print("1 :", j)
                ascii2.append(j)

            elif ord("a") <= j <= ord("z"):
                j = j + n
                if ord("z") < j:
                    j = j - 26
                j = chr(j)
                print("2 :", j)
                ascii2.append(j)

        else:
            j = chr(j)
            ascii2.append(j)

    answer = "".join(ascii2)
    return answer

#print(solution(s1, n1))
#print(solution(s2, n2))
#print(solution(s3, n3))     # s3 = "a B z",   n = 4
#print(solution(s4, n4))
print(solution(s5, n4))

