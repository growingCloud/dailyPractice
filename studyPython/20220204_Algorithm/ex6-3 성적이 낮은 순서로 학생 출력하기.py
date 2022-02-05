# 이코테 예제 6-3 성적이 낮은 순서로 학생 출력하기
# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과
# 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오

# [입력 예시]
# 2
# 홍길동 95
# 이순신 77

# [출력 예시]
# 이순신 홍길동

count = int(input())
student, scores = {}, []

for _ in range(count):
    name, score = input().split()
    student[score] = name   # append 형태로 바꿔주기 ! 점수 같으면 겹쳐버림 ....
    scores.append(score)

scores.sort()

print(scores)
print(student)

for s in scores:
    print(student[s], end=" ")
