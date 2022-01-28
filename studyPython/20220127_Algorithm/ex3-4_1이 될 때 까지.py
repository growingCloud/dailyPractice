# 이코테 예제 3-4 1이 될 때 까지
# 어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여
# 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.

# 1. N 에서 1을 뺀다.
# 2. N을 K로 나눈다.

# N과 K가 주어질 때 N이 1이 될 때 까지
# 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오

import sys

target, divisor = map(int, sys.stdin.readline().split())
count = 0

while True:
    if target % divisor == 0:
        target = target // divisor
        count += 1

    elif target % divisor != 0:
        target = target - 1
        count += 1

    elif target == 1:
        break

print(count)