nums = int(input())
picked = int(input())

# 중복순열 뽑는 DFS
def DFS_1(Level, res):
    if Level == picked:
        print(res)
        return
    for n in range(1, nums + 1):
        DFS_1(Level + 1, res + [n])

DFS_1(0, [])

# 중복을 제거한 순열을 뽑는 DFS
def DFS_2(Level, res, selected):
    if Level == picked:
        print(res)
        return
    for n in range(1, nums + 1):
        if n in selected:
            continue
        DFS_2(Level + 1, res + [n], selected + [n])


DFS_2(0, [], [])


# 조합 숙제 (토요일까지)
# 조합 : 서로 다른 n개의 원소를 가지는 어떤 집합에서 순서에 상관없이 r개의 원소를 선택하는 것

# 중복조합 뽑는 DFS
def DFS_3(Level, res):
    if Level == picked:
        print(res)
        return
    for n in range(1, nums + 1):
        DFS_3(Level + 1, res + [n])

DFS_3(0, [])

# 중복을 제거한 조합을 뽑는 DFS
def DFS_4(Level, res, selected):
    if Level == picked:
        print(res)
        return
    for n in range(1, nums + 1):
        if n in selected:
            continue
        DFS_4(Level + 1, res + [n], selected + [n])

DFS_4(0, [], [])