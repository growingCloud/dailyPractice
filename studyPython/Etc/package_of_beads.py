# Alice 파이썬 문제집_구슬 꾸러미 문제

# 지시사항을 참고하여 코드를 작성하세요.
# 빨간 구슬 = 250g
# 파란 구슬 = 40g
# 흰 구슬 = 10g

# 300g의 꾸러미를 만들기 위해서는 빨간 구슬 1개, 파란 구슬 1개, 흰 구슬 1개로 최소 3개의 구슬이 필요합니다.
# 사용자로부터 구슬 꾸러미의 무게를 입력받고 꾸러미를 만드는 데 사용되는 최소 구슬의 수를 출력하세요.
# 입출력 예시 (300 -> 3), (550 -> 4), (65 -> -1)

weight = int(input())

Big_Q, Mid_Q, Sml_Q = 0, 0, 0   # 사이즈별 나눈 몫
Big_R, Mid_R, Sml_R = 0, 0, 0   # 사이즈별 나눈 나머지

Big_Q = weight // 250
Big_R = weight % 250

Mid_Q = Big_R // 40
Mid_R = Big_R % 40

Sml_Q = Mid_R // 10
Sml_R = Mid_R % 10

count = 0

if Big_Q == 0 :         # 250보다 작은 무게
    if Mid_Q == 0 :     # 40보다 작은 무게
        if Sml_Q == 0:  # 10보다 작은 무게
            print(-1)
        elif Sml_Q == 0 and Sml_R != 0 :
            print(-1)
        else :          # 10의 배수
            count = count + Sml_Q
            print(count)
    
    else :   # 40보다 큰 무게
        if Sml_Q == 0:  # 10보다 작은 무게
            print(-1)
        elif Sml_Q == 0 and Sml_R != 0 :
            print(-1)
        elif Sml_Q != 0 and Sml_R != 0 :
            print(-1)
        else :
            count = count + Sml_Q
            print(count)
    


else :
    count = count + Big_Q
    if Mid_Q == 0 : 
        if Sml_Q == 0:  # 10보다 작은 무게
            print(-1)
        elif Sml_Q == 0 and Sml_R != 0 :
            print(-1)
        elif Sml_Q != 0 and Sml_R != 0 :
            print(-1)
        else : 
            count = count + Sml_Q
            print(count)
    
    else :
        count = count + Mid_Q
        if Sml_Q == 0:  # 10보다 작은 무게
            print(-1)
        elif Sml_Q == 0 and Sml_R != 0 :
            print(-1)
        elif Sml_Q != 0 and Sml_R != 0 :
            print(-1)
        else :
            count = count + Sml_Q
            print(count)