# 이코테 예제 3-2 큰 수의 법
# 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때
# 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오

# 입력조건 >> 첫째 줄에 N (2 <= N <= 1,000), M (1 <= M <= 10,000), K (1 <= K <= 10,000)의
#           자연수가 주어지며, 각 자연수는 공백으로 구분한다.
#           둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
#           입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건 >> 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 입력 예시 >> 5 8 3, 2 4 5 4 6
# 출력 예시 >> 46
import sys

numbers, count, limit = map(int, sys.stdin.readline().split())
num_str = sys.stdin.readline().split()
num_li = []
for n in num_str:
    num_li.append(int(n))

num_li.sort(reverse = True)
sum = 0
limit_c = limit

max_first = num_li[0]
max_second = num_li[1]

while True:
    sum = sum + max_first
    count = count - 1
    limit_c = limit_c - 1

    if limit_c == 0:
        sum = sum + max_second
        count = count - 1
        limit_c = limit

    if count == 0 :
        break

print(sum)

# 0번째 인덱스를 넣는다. (limit 까지 더해줌, 더할 때 마다 카운트 1)
# 리미트 도달하면 다음 숫자를 하나 넣는다 (Index(1))
# 카운트가 끝나면 더한 값을 반환한다.

