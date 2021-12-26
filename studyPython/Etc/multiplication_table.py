# 1. 반복문을 활용하여 구구단 2단을 출력해 보기

i = 1

while i <= 9 :
    two = 2 * i
    print("2 x {} = {}".format(i, two))
    i += 1
print("구구단 2단 끝!")
print()


# 2. 1번의 구문을 입력으로 바꿔서 입력한 구구단이 출력되도록 하기
dan = int(input("숫자 입력 : "))
i = 1

while i <= 9 :
    print("{} x {} = {}".format(dan, i, dan * i))
    i += 1
print("구구단 끝!")
print()


# 3. 구구단 2단을 역순으로 출력해보기!
i = 9


while i >= 1 :
    two = 2 * i
    print("2 x {} = {}".format(i, two))
    i -= 1
print("구구단 2단 끝!")
print()


# 4. 정수를 하나 입력 받아서 1 ~ n까지 일렬로 출력
# ex : 입력 : 5 -> 출력 : 1 2 3 4 5

num = int(input("숫자 입력 : "))
i = 1
total = 0

while i <= num :
    print(i, end = " ")

    total += i      # 반복숫자가 누적되도록
    i += 1

print("({})".format(total))



# 연습) for 문을 활용해서 풀어주세요

# 1. 구구단 2단을 출력하라. 단, x1 ~ x9까지
# 2. 1번을 입력으로 바꿔서, 입력받은 구구단을 출력하라


# 3. 구구단을 역순으로 출력
for i in range(1, 10) : 
    print("2 x {} = {}".format(i, i * 2))
print("구구단 2단 끝!")
print()


# 2. 1번의 구문을 입력으로 바꿔서 입력한 구구단이 출력되도록 하기
dan = int(input("숫자 입력 : "))
for i in range(1, 10) : 
    print("{} x {} = {}".format(dan, i, dan * i))
print("구구단 끝!")
print()


# 3. 구구단 2단을 역순으로 출력해보기!
for i in range(9, 0, -1) : 
    print("2 x {} = {}".format(i, i * 2))
print("구구단 2단 끝!")
print()