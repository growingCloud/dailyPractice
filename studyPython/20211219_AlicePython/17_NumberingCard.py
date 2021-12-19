# 17. 끼리끼리
# 1. 첫 번째 줄에 카드의 수를 나타내는 정수가 입력됩니다. 두 번째 줄부터 n개의 줄에 걸쳐서, 각 카드에 적힌 숫자가 입력됩니다. 
#    각 숫자는 정수형 값으로 변환하여 리스트 card에 저장하세요.
# 2. 입력받은 순서대로 0 이상인 경우 리스트 red_pocket에, 0 미만인 경우 리스트 blue_pocket에 저장하세요.
# 3. 각각의 주머니에 카드를 모두 담은 뒤 리스트 card_box에 순서대로 리스트 red_pocket, 리스트 blue_pocket을 저장하세요.


# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
card = []
red_pocket = []
blue_pocket = []
card_box = []

# 지시사항 1번을 참고하여 코드를 작성하세요.
count = int(input())
for i in range(count) :
    card.append(int(input()))


# 지시사항 2번을 참고하여 코드를 작성하세요.
for num in card :
    if num < 0 :
        blue_pocket.append(num)
    else :
        red_pocket.append(num)
        
# 지시사항 3번을 참고하여 코드를 작성하세요.
card_box.append(red_pocket)
card_box.append(blue_pocket)


# 아래 코드는 결과를 확인하기 위한 코드입니다.
print(card_box)