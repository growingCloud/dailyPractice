# ************(미완료)**********************

# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)
            return

        node = self.front
        while node and node.next:
            node = node.next    # node.next가 None이 될때 까지
        node.next = Node(value, None)

    def pop(self):
        if self.front is None:
            return None

        frontNode = self.front
        self.front = self.front.next
        return frontNode.item

numbers1 = [1,2,3,4,6,7,8,0]
numbers2 = [5,8,4,0,6,7,9]
result = []

numbers1.sort()

print(numbers1)
queue = Queue()

for i in numbers1:
    print(i)
    queue.push(i)
    print(queue)

std = 0
for std in range (10):
    if queue.pop() == std:
        continue
    elif queue.pop() != std:
        result.append(std)
        print(result)









print(result)