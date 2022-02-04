# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

arr1 = [4,3,2,1]
arr2 = [10]

def solution(arr):
    arr.pop(arr.index(min(arr)))
    if len(arr) == 0: return [-1]

    return arr

# print(solution(arr1))
# print(solution(arr2))


# -----------------------------------[이선생님 람다식 어시스트]

solution2 = lambda x : x if len(x) > 1 and float('inf') + x.pop(x.index(min(x))) else [-1]

# float('inf') : 양의 무한대수

print(solution2(arr1))
print(solution2(arr2))