def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        li = array[(commands[i][0] - 1):(commands[i][1])]
        li.sort()
        print(li)

        idx = commands[i][2]
        print(idx)

        a = li[idx - 1]
        answer.append(a)

    return answer