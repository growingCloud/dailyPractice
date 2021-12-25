# 03. 소수 만들기 - Ex
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# 입출력 예
# nums	    result
# [1,2,3,4]	    1
# [1,2,7,6,4]	4

# 원래는 위의 문제였으나, 문제를 잘못 이해하여, 입력한 숫자 중 소수를 찾고,
# 그 소수 안에서 랜덤으로 3개를 뽑아 합을 구하는 코드를 작성 해 버렸음... 고민한 부분이 아까워 1일 1커밋에 올림!

import random

primes = []
choice = set()

for i in range(1000) :
    count = 0
    for j in range(1, i + 1) :
        if i % j == 0 :
            count += 1
    if count == 2 :
        primes.append(i)


# 랜덤으로 소수를 골라서 Set에 담기 (중복 제거)

for i in range(10) :
    choice.add(random.choice(primes))
    if len(choice) == 3 :
        break

choice = list(choice)
result = sum(choice)


print(choice)
print(result)
