# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
# 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다.

# 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다.
# (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):
    day = 1

    for i in range(a):
        if i in (1, 3, 5, 7, 8, 10, 12): day += 31
        if i in (4, 6, 9, 11): day += 30
        if i == 2: day += 29
        if i == 0: pass

    result_day = (day + (b - 1)) % 7
    week = {2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU", 1: "FRI"}

    answer = week[result_day]
    return answer


print(solution(1, 1))
print(solution(5, 24))


day = 1 + 31 + 29 + 31 + 30 + (24 - 1)
#   기본 + 1월 + 2월 + 3월 + 4월 + 남은 일
result_day = (day) % 7
print(result_day)
week = {2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU", 1: "FRI"}

answer = week[result_day]
print(answer)