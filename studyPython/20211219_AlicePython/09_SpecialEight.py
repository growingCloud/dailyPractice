# 08. 8은 특별해!
# 1부터 10,000까지의 수 중 8이 등장하는 횟수를 세어 출력하세요.

li = []
number = []

for i in range (10000) :
    li.append(i)

string1 = list(map(str, li))
#print(string1)

string2 = ''.join(string1)
#print(string2)

print(string2.count('8'))
