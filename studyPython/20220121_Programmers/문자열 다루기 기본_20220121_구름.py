# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# s는 길이 1 이상, 길이 8 이하인 문자열입니다.

s1 = "a234"
s2 = "1234"

if (len(s1) == 4 or len(s1) == 6) and s1.isdigit() == True :


# -------------------------------- [이선생님 어시스트]

solution = lambda x: True if (len(x) in (4, 6) and x.isdigit()) else False