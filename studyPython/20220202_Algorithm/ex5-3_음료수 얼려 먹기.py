# 이코테 예제 5-3 음료수 얼려 먹기
# N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
# 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

# [입력 예시]
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

# [출력 예시]
# 8

# N, M을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append((list(map(int, input()))))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def DFS(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y > m:
        return False
