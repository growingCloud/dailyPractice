# 13. 우뚝 솟은 빌딩! 함께 만들어볼까요?

# 1번째 줄 부터 5번째 줄 까지는 별을 각각 1, 2, 3, 4, 5개 출력합니다.
# 6번째 줄부터는 별을 항상 5개 출력합니다.
# 입출력 예시 : 7 
# *
# **
# ***
# ****
# *****
# *****
# *****


num = int(input())
if num <= 5 :
    for i in range (num) :
        print('*' * (i+1), end="")
        print()
if num > 5 :
    for i in range (5) :
        print('*' * (i+1), end="")
        print()
    for i in range (5, num) :
        print('*****')





