# 이코테 예제 4-1 상하좌우
# 여행가 A는 N * N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 * 1 크기의 정사각형으로
# 나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아 좌표는 (N, N)에 해당한다.
# 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리
# 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있다.

# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# 이때 여행가 A가 N * N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
# 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시된다. 다음은 N = 5인 지도와 계획서이다.
# 이 경우 6개의 명령에 따라서 여행가가 움직이게 되는 위치는 순서대로 (1, 2), (1, 3), (1, 4),
# (1, 4), (2, 4), (3, 4) 이므로, 최종적으로 여행가 A가 도착하게 되는 곳의 좌표는 (3, 4)이다.
# 다시 말해 3행 4열의 위치에 해당하므로 (3, 4)라고 적는다. 계획서가 주어졌을 때 여행가 A가
# 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오

# [입력 예시] 5, R R R U D D
# [출력 예시] 3, 4

size = int(input())
moving = input().split()

print(size)
print(moving)

direction_x = {'L': 0, 'R': 0, 'U': -1, 'D': 1}
direction_y = {'L': -1, 'R': 1, 'U': 0, 'D': 0}

my_x = 1
my_y = 1

for d in moving:
    check_x = my_x + direction_x[d]
    check_y = my_y + direction_y[d]

    if check_x < 1 or check_x > size or check_y < 1 or check_y > size :
        print('moving 1 :', my_x, my_y)
        continue
    print('moving 2 :', my_x, my_y)

    my_x = check_x
    my_y = check_y

print(my_x, my_y)