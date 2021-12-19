# 12. 냉정과 열정 사이에 있는 사랑의 개수는?
# 아래 내용을 읽고 hot_cold함수를 올바르게 구현하세요.

# hot_cold 함수에는 매개변수로 리스트 emotion이 주어집니다. 이 리스트의 원소는 모두 문자열 “냉정”, “열정”, “사랑” 중 하나임이 보장됩니다.
# hot_cold는 emotion의 “냉정” 원소와 “열정” 원소 사이의 “사랑” 이 모두 몇 개인지 계산하여, “사랑”의 개수를 정수 자료형으로 반환합니다.

# 입출력 예시 (hot_cold(['냉정', '사랑', '사랑', '사랑', '열정', '사랑', '사랑']) -> 3) 
#            (hot_cold(['열정', '사랑', '사랑', '사랑', '냉정', '사랑', '사랑']) -> 3)


def hot_cold(emotion) :
    cold = 0
    hot = 0

    for i in emotion :
        if i == '냉정' :
            cold = emotion.index(i)
        if i == '열정' :
            hot = emotion.index(i)
        
        num = cold - hot
        result = abs(num) - 1
        
    return result


print(hot_cold(['냉정', '사랑', '사랑', '사랑', '열정', '사랑', '사랑']))

print(hot_cold(['열정', '사랑', '사랑', '사랑', '냉정', '사랑', '사랑']))