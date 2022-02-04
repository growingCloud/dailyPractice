# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한
# 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

phone_number1 = "01033334444"
phone_number2 = "027778888"
phone_number3 = "0123456789123456789"

def solution(phone_number):
    li_1 = list(phone_number)
    li = []

    for i in range(len(li_1) - 4) :
        li.append('*')

    for j in range(4, 0, -1) :
        li.append(li_1[- (j)])

    answer = "".join(li)
    return answer


print(solution(phone_number1))
print(solution(phone_number2))
print(solution(phone_number3))
