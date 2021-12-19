# 07. 엘리스 토끼의 수학 숙제
# 사용자로부터 자연수를 입력받아 1부터 입력받은 수까지의 합의 제곱과 제곱의 합의 차이를 계산하여 출력하세요.
# 출력 결과는 정확히 정수 하나만 출력되어야 합니다.

# 합의 제곱 수식
# 2(1 + 2 + 3 + ・・・ 8 + 9 + N)^2
 
# 제곱의 합 수식
# 1^2 + 2^2 + 3^2 + ... + 8^2 + 9^2 + N^2

# 입출력 예시 (10 -> 2640)

num = int(input())

ok_sum = 0
ng_sum = 0

for i in range(num + 1) :
    ok_sum += i
    # print(i, ":", ok_sum)
ok = (ok_sum) ** 2
# print(ok)

    
for j in range(num + 1) :
    ng_sum = ng_sum + (j ** 2)
    # print(j, ":", ng_sum)
ng = ng_sum
# print(ng)

print(ok - ng)

