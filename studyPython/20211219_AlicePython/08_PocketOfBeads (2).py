# 08. 구슬 꾸러미
# 엘리스 토끼는 구슬 장사를 위해 구슬을 꾸러미에 담아 포장을 하고 있습니다. 엘리스 토끼가 준비한 구슬은 색상별로 무게가 모두 다르며 
# 구슬 꾸러미 또한 구슬을 담아낼 수 있는 무게가 모두 달라 최소한의 구슬 개수를 활용해 꾸러미를 채우려고 합니다.
# 색깔과 무게가 다른 3가지 종류의 구슬이 무제한으로 주어집니다.

# 빨간 구슬 : 250g
# 파란 구슬 : 40g
# 흰 구슬 : 10g

# 사용자로부터 구슬 꾸러미의 무게를 입력받고 꾸러미를 만드는 데 사용되는 최소 구슬의 수를 출력하세요. (1 ≤ 구슬 꾸러미 무게 ≤ 10,000)
# 만약 무게에 맞추어 꾸러미를 만들 수 없는 경우에는 -1을 출력하세요.


weight = 0

# Create valuable
red = 250
blue = 40
white = 10
    
# Init res value is -1, when weight under 300
res = 0
    
# Input weight
weight = int(input())
    
res = 0
remain = weight % red        
res += weight // red
        
res += remain // blue
remain = remain % blue
res += remain // white
remain = remain % white
# result value is res
    
print(res)
