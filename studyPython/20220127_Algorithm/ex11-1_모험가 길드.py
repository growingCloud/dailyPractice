# 한 마을에 모험가가 N명 있습니다. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정 했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는
# 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
# 동빈이는 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금합니다.

# 동빈이를 위해 N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의
# 최댓값을 구하는 프로그램을 작성하세요

# [입력 예시] 5, 2 3 1 2 2
# [출력 예시] 2

adventurer = int(input())
fear = list(map(int, input().split()))

fear.sort()

members = []
team_count = 0

for i in fear:
    members.append(i)
    if len(members) >= i:
        team_count += 1
        members = []

print(team_count)
