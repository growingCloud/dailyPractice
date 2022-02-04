# ************(미완료)**********************

# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와
# 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다.
# 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# progresses1 = [93, 30, 55]
# speeds1 = [1, 30, 5]            # return = 	[2, 1]

progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]    # return = 	[1, 3, 2]

# 100애서 모든 진도율 빼기
# 남은 진도율을 스피드로 나누기 (나머지 남으면 1 더해주는거 잊지말기)
# 그 중 가장 오래걸리는 것이 배포일인데,
# 만약 인덱스 0번이 제일 오래 걸린다면 그거 기준으로 무조건 따라감

# 투포인터로 해야하나...?

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

remains = []
d_days = []
queue = Queue()


for p in progresses2:
    percent = 100 - p
    # remains.append(percent)  >> remains = [7, 70, 45]
    queue.push(percent)
    print(percent)
    print(queue)

for s in speeds2:
        remains_num = queue.pop()
        big = remains_num // s
        small = remains_num % s

        if small != 0: big += 1
        d_days.append(big)


print(d_days)

# 기준 수보다 다음 수가 작으면 카운트 1 하고 pop?
# 기준 수보다 다음 수가 크면 카운트 안하고 curr을 next로 넘겨주기?
# 슬라이싱?!?!?!?!?!?!?



result = []
# for i in range (1, len(d_days)):
#     left = i - 1
#     right = i
#
#     if d_days[left] < d_days[right]:
#         cut = d_days[left:right]
#         print(cut)
#         result.append(len(cut))
#     if d_days[left] > d_days[right]:
#        pass
#     right += 1





