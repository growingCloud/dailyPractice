# 03. In the Middle
# 세 개의 정수를 입력받아 중간값을 출력하세요. 각 줄에 걸쳐서 정수가 하나씩 입력됩니다.
# 입출력 예시 (1, 3, 2 -> 2)

n1 = int(input())
n2 = int(input())
n3 = int(input())

li = []

li.append(n1)
li.append(n2)
li.append(n3)

li.sort()

print(li[1])
