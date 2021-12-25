# 03. 소수 만들기 (미완료)
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

# 입출력 예
# nums	    result
# [1,2,3,4]	    1
# [1,2,7,6,4]	4

import random

# def solution(nums):
    #return answer
answer = 0
three = []
li = []
nums = [1,2,7,6,4]
n = len(nums)

for i in range (100000) :
    while (len(three) == 4) :
        for i in range (3) :
            three.append(random.choice(nums))
        three = []
        

    li.append(set(three))


    if len(li) == n*(n-1)*(n-2) :
        break
            
print(li)
print(len(li))


# solution([1,2,3,4])
# solution([1,2,7,6,4])

# 내가 생각한 알고리즘
# 1. 5개 (n개) 중에서 3개 뽑기
# 2. 중복 없이 모든 경우의 수만큼 뽑아서 리스트에 저장
# 3. 원소 갯수만큼 원소의 sum 구해서 새 리스트에 넣기
# 4. 리스트 안의 원소들 소수인지 판별하기
# 5. 판별한 소수의 갯수를 반환