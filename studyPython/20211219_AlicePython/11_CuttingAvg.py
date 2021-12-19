# 11. 절사평균을 구해봅시다!
# 절사평균은 최댓값과 최솟값을 제외한 값들의 평균을 의미합니다. 
# 어떤 리스트가 주어질 때, 우리는 그 리스트의 절사평균을 구하려고 합니다. 절사평균을 구하는 함수 myMean()를 만들어봅시다.


def myMean(li) :
    
    li.remove(max(li))
    li.remove(min(li))
    
    result = sum(li) / len(li)
    
    return result

print(myMean([1, 2, 3, 4, 5]))
