# 이코테 예제 12-8 문자열 재정렬
# 알파벳 대문자와 숫자 (0 ~ 9) 로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

# 예를 들어 K1KA5CB7이라는 값이 들어오면, ABCKK13을 출력합니다.

# [입력 예시 1] K1KA5CB7
# [출력 예시 1] ABCKK13

# [입력 예시 2] AJKDLSI412K4JSJ9D
# [출력 예시 3] ADDIJJJKKLSS20

inputs = list(input())

strs = [s for s in inputs if s.isalpha()]
nums = [n for n in inputs if n.isdigit()]

strs.sort()
sum_num = 0

for m in nums:
    sum_num += int(m)

result = "".join(strs) + str(sum_num)

print(result)