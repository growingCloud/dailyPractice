# 이코테 예제 12-11 뱀
#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
#  뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다.
# 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

# 1) 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 2) 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 3) 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 4) 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

# [입력 예시]
# 6         보드의 크기
# 3         사과의 개수
# 3 4       사과 위치 1
# 2 5       사과 위치 2
# 5 3       사과 위치 3
# 3         변환 횟수
# 3 D       변환 1 (오른쪽)
# 15 L      변환 2 (왼쪽)
# 17 D      변환 3 (오른쪽)

# [출력 예시] 9


# 보드 만들기
size = int(input())
board = [[0 for col in range(size)] for row in range(size)]
print(board)

# 사과 배치하기 (apple = 1)
apple = int(input())
for a in range(apple):
    r_apple, c_apple = map(int, input().split())
    board[r_apple - 1][c_apple - 1] = 1
print(board)


# 방향 변환 횟수에 따라 움직이기
board_direction = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}
snake = board[0][0]
turn_count = int(input())
for m in range(turn_count):
    s_move, s_direction = map(int, input().split())

