# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

# 입력 1 >> [2,1,3,4,1]  출력 1 >> [2,3,4,5,6,7]
# 입력 2 >> [5,0,2,7]  출력 2 >> [2,5,7,9,12]

import itertools

def solution(numbers):
    all_things =  list(itertools.combinations(numbers,2))
    sum_li = []

    for i in range(len(all_things)):
        a = sum(all_things[i])
        sum_li.append(a)


    set_li = set(sum_li)
    answer = list(set_li)
    answer.sort()

    return answer


print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))