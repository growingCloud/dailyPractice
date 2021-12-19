# 10. 문자열 앞뒤 검사하기
# 사용자로부터 문자열을 입력받고 문자열의 앞에서 i번째 문자와 뒤에서 i번째 문자가 같은지 비교한 후 
# 두 문자가 같다면 Same을, 다르다면 Different를 출력합니다.
# 문자열은 알파벳 소문자로만 이루어져 있고 길이는 반드시 짝수입니다.


string = list(input())
count = 0

for i in range(int(len(string) / 2)) :
    if string[i] == string[-(i + 1)] :
        print("Same")
    else : 
        print("Different")

