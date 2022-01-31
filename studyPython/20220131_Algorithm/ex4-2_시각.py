# 이코테 예제 4-2 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도
# 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 1을 입력했을 때 다음은 3이
# 하나라도 포함되어 있으므로 세어야 하는 시각이다.

# 00시 00분 03초
# 00시 13분 30초

# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안되는 시각이다.

# 00시 02분 55초
# 01시 27분 45초

# [입력 예시] 5
# [출력 예시] 11475
hour = int(input())

count = 0

for h in range(hour + 1):
    for m in range(60):
        for s in range(60):
            if str(s).find('3') != -1 or str(m).find('3') != -1 or str(h).find('3') != -1:
                count += 1

# for h in range (hour + 1):
#     if str(h).find('3') != -1:
#         count += 1
#     for m in range (60):
#         if str(m).find('3') != -1:
#             count += 1
#         for s in range(60):
#             if str(s).find('3') != -1:
#                 count += 1
# 해답보다 작게 나올 수 밖에 없음 >> 0시 기준으로 0~60분 안에 3이 몇개 있는지 구하는것, 중복을 고려하지 않음

print(count)