# 05. 말썽쟁이 도도새
# 문자열이 들어있는 리스트를 vomit()함수에 넣었을 때, 도도새가 아팠던 시점을 계산하여 그전까지 복통이 지속된 시간을 반환하는 vomit() 함수를 작성하세요. 
# vomit() 함수의 반환값은 정수 자료형이어야 합니다.
# 주어지는 리스트에, "웩"은 단 하나만 존재합니다.
# 입출력 예시 : (vomit(['과자', '과자', '과자', '커피', '과자', '웩', '음료수', '음료수', '과자', '커피', '커피', '커피']) -> 5)

def vomit (list) :
    count = 0
    
    for i in list :
        if i != '웩' :
            count +=1
        else :
            print(count)
            return count



vomit(['과자', '과자', '과자', '커피', '과자', '웩', '음료수', '음료수', '과자', '커피', '커피', '커피'])

