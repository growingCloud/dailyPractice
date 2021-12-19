# 18. 렌터카
# 엘리스 토끼는 제주도에 놀러 와 H 시간만큼 렌터카를 빌리려고 합니다. 
# 제주도의 대표 렌터카 업체인 모자장수 렌터카와 코더랜드 렌터카는 모두 같은 차량을 제공하고 있지만, 이용 요금에 차이가 있어 가격을 비교해보려고 합니다.

# 모자장수 렌터카 : 1시간당 A 원에 사용
# 코더랜드 렌터카 : 기본요금 B 원에 기본 C 시간 사용, C 시간이 넘어가면 시간당 D 원의 추가 요금 부과

# 1. 첫 번째 줄에 엘리스 토끼가 렌터카를 이용할 시간을 나타내는 정수가 입력됩니다. 이 값을 변수 H에 저장하세요.
# 2. 두 번째 줄에 모자장수 렌터카의 시간당 비용을 나타내는 정수가 입력됩니다. 이 값을 변수 A에 저장하세요.
# 3. 그리고 세 번째 줄 부터 각 줄에 걸쳐, 코더랜드 렌터카의 기본요금, 기본 시간, 기본 시간 이후에 시간당 부과되는 요금을 나타내는 정수가 입력됩니다. 
#    이 값들을 각각 변수 B, C, D에 저장하세요.
# 4. 두 업체의 정보를 토대로 비교하여 최소 비용을 변수 result에 저장하세요.
#    입력받는 모든 수는 자연수이며 범위는 다음과 같습니다. (1 ≤ A, B, C, D, H ≤ 10,000)


# 지시사항 1~3번을 참고하여 코드를 작성하세요.
H = int(input())    # 렌터카 이용시간
A = int(input())    # 모자, 시간당 비용
B = int(input())    # 코더, 기본요금
C = int(input())    # 코더, 기본 사용시간
D = int(input())    # 코더, 시간당 추가 비용

# 지시사항 4번을 참고하여 코드를 작성하세요.
hat = H * A

if H > C :
    coder = B + D * (H - C)
else :
    coder = B

li = [hat, coder]

result = min(li)



# 아래 코드는 결과를 확인하기 위한 코드입니다.
print(result)