# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# s는 길이가 1 이상, 100이하인 스트링입니다.

s1 = "abcde"
s2 = "qwer"


def solution(s):
    li = list(s)

    half = len(li) // 2
    counter =len(li) % 2

    answer = "".join(li)

    if counter == 1: return answer[half]
    else : return answer[half-1 : half+1]

print(solution(s1))
print(solution(s2))