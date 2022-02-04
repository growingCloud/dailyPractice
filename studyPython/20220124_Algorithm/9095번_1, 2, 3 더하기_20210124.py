# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# input : 4
# output : 1+1+1+1, 1+1+2, 1+2+1,
#          2+1+1, 2+2, 1+3, 3+1

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

input = 4
# make(4) = make(3) + make(2) + make(1)


def make(n):
    if n == 1:
        return 1    # 1을 만드는 경우의 수 1가지 [1]
    if n == 2:
        return 2    # 2을 만드는 경우의 수 2가지 [1, 1], [2]
    if n == 3:
        return 4    # 3을 만드는 경우의 수 4가지 [1, 1, 1] [2, 2] [1, 3] [3, 1]
    return make(n - 1) + make(n - 2) + make(n - 3)

print(make(4))
print(make(7))



# -----------------------------------------[이선생님 홈런]


def operator(num):
    board = [0] * num  # 모두 1로 num을 만들었을 경우, num개가 필요하므로 board의 길이를 num으로 한다.
    cnt = 0

    def dfs(i):  # i는 i번째를 채울 것임을 의미한다. 즉 dfs(3)이 구동되는 것은 board가 0, 1이 채워진 상태.
        s = sum(board[:i])  # board는 계산 과정에서 계속 변화하고, 최초로 탐색할 때는 문제가 없으나
        # 그 이후에는 숫자가 board에 남아 문제가 생긴다.
        # 이는 list를 변조하는 과정에서 해당 참조 위치에 있는 값 자체에 변동이 생기기 때문이다.
        # 이를 해결하기 위해서 [:i]로 sum을 구할 대상을 제한한다.

        if s == num:  # 여기서 num과 sum(board)를 비교하면 앞서 말한 문제가 생기게 된다.
            print(board[:i])
            # print(board) # 이렇게 실행하면, board 전체가 모두 출력되는데, 이 경우 이전 연산의 결과로 남은 불필요한 뒷부분이 출력된다.

            nonlocal cnt  # 해당 함수 한단계 위의 변수에 접근 가능하도록 nonlocal을 적어준다.
            cnt += 1
        else:
            for j in range(1, 4):
                if s + j > num:  # i번쨰 숫자에 j를 끼워넣을 예정이다. 따라서, 숫자가 num을 초과하는 경우에 무시한다.
                    continue
                else:  # 초과하지 않는 경우에는 j를 추가하고, i+1번째 문자를 채우기 위해 dfs(i+1)을 실행한다.
                    board[i] = j
                    dfs(i + 1)

    dfs(0)
    print(cnt)
    return


operator(10)  # 실험을 위한 코드 실행