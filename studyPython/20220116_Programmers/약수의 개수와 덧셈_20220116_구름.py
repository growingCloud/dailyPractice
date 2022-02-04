# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고,
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000

def solution(left, right):
    answer = 0
    count = 0
    li_p, li_m = [], []

    for i in range(left, right + 1):
        # i의 약수를 구하는 내용이 아래로
        for j in range(i):
            if i % (j + 1) == 0:
                count += 1
            else:
                pass

        if count % 2 == 0:
            # li_p.append(i)
            print(li_p)
        else:
            # li_m.append(i)
            print(li_m)

    left_s = sum(li_p)
    # print(left_s)
    right_s = sum(li_m)
    # print(right_s)

    answer = left_s - right_s

    return answer