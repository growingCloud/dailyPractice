'''
날짜 : 2021년 12월 16일
시작시각 : 오후 2시 16분 
끝난시각 : 오후 2시 56분    (40분 소요)

맨날 보면서도 바로바로 안풀리는 중첩 반복문으로 별찍기 연습.
다 풀면 입력으로 바꿔서 만들어보자!

1. N x N 별찍기를 수행한다  //  2. 직각 삼각형

*****    *
*****    **
*****    ***
*****    ****
*****    *****

3. 2번을 위아래 반전 // 4. 2번을 좌우 반전 // 5. 피라미드  // 6. 역 피라미드
'''

# 1. 5 x 5 별찍기를 수행한다

for i in range (5) : 
    for j in range (5) : 
        print('*', end ="")     # 열에 별 5번 찍어주고 줄바꿈 제거하는 end
    print()                     # 다음 행으로 넘어가기 전 줄바꿈 처리
print() 


# 2. 직각 삼각형

for i in range (5) : 
    for j in range (i + 1) :    # 1번과 같은 대신, i + 1 만큼 별이 찍히도록 함
        print('*', end ="")
    print()
print() 


# 3. 2번을 위아래 반전

for i in range (5, 0, -1) :     # 2번과 같은 대신, 역으로 별이 찍히도록 함
    for j in range (i) :
        print('*', end ="")
    print()
print() 


# 4. 2번을 좌우 반전
count = 5

for i in range (5) : 
    for j in range (i) :        
        print(end =" ")         # 2번을 활용해서 별 대신 공백으로 채움
    for j in range (count) :    # count를 활용한 증감식을 통해 그 뒤에 별이 찍히도록 함
        print('*', end ="")
    count -= 1
    print()
print() 


# 5. 피라미드 

for i in range(5) :
    for j in range(4 - i) :
        print(end =" ")         # 4번을 활용해서 역순으로 공백 채움
    for j in range(2 * i + 1) : # 홀수 갯수의 별이 찍히도록 범위 설정
        print(end ="*")
    print()
print()


# 6. 역 피라미드

for i in range(5, 0, -1) :
    for j in range(5 - i) :
        print(end =" ")
    for j in range(2 * i - 1) :
        print(end ="*")
    print()
print()
