# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며,
# 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
# 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	            []	            []	        [7,4,5,6]
# 1~2	        []	            [7]	        [4,5,6]
# 3	            [7]	            [4]	        [5,6]
# 4	            [7]	            [4,5]	    [6]
# 5	            [7,4]	        [5]	        [6]
# 6~7	        [7,4,5]	        [6]	        []
# 8	            [7,4,5,6]	    []	        []

# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.
#
# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length,
# 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다.
# 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

bridge_length1 = 2
weight1 = 10
truck_weights1 = [7,4,5,6]      # return = 8

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10]           # return = 101

bridge_length3 = 100
weight3 = 100
truck_weights3 = [10,10,10,10,10,10,10,10,10,10]    # return = 110


bridge = []
count = 0

# 0으로 아무것도 없는 빈 공간의 다리 만들기
for space in range(bridge_length1):
    bridge.append(0)

print(bridge)

# 1번 트럭 출입, 카운팅까지 얘네들은 한 세트!
bridge.append(truck_weights1[0])
bridge.pop(0)
count += 1
print("1 :", bridge)
print("1 :", sum(bridge))

# 빈공간 투입 , 카운팅까지 얘네들은 한 세트!
bridge.append(0)
bridge.pop(0)
count += 1
print("2 :", bridge)
print("2 :", sum(bridge))

# 2번 트럭 출입, 카운팅까지 얘네들은 한 세트!
bridge.append(truck_weights1[1])
bridge.pop(0)
count += 1
print("3 :", bridge)
print("3 :", sum(bridge))

# 3번 트럭 출입, 카운팅까지 얘네들은 한 세트!
bridge.append(truck_weights1[2])
bridge.pop(0)
count += 1
print("4 :", bridge)
print("4 :", sum(bridge))

# 빈공간 투입 , 카운팅까지 얘네들은 한 세트!
bridge.append(0)
bridge.pop(0)
count += 1
print("5 :", bridge)
print("5 :", sum(bridge))

# 4번 트럭 출입, 카운팅까지 얘네들은 한 세트!
bridge.append(truck_weights1[3])
bridge.pop(0)
count += 1
print("6 :", bridge)
print("6 :", sum(bridge))

# 빈공간 투입 , 카운팅까지 얘네들은 한 세트!
bridge.append(0)
bridge.pop(0)
count += 1
print("7 :", bridge)
print("7 :", sum(bridge))

# 빈공간 투입 , 카운팅까지 얘네들은 한 세트!
bridge.append(0)
bridge.pop(0)
count += 1
print("8 :", bridge)
print("8 :", sum(bridge))
print(count)
print()

# sum(bridge)가 10이 넘지 않으면 트럭을 밀어넣어주고, 10 이상이되면 0을 밀어넣어준다 !!!
# 언재까지 밀어 넣어줘야해? >> len(truck_weights) + @ 만큼!

count = 0

for i in truck_weights1 :
    if sum(bridge) > weight1 :
        bridge.append(0)
        bridge.pop(0)
        count += 1
        print(bridge)
        print(sum(bridge))

    elif sum(bridge) <= weight1 :
        if sum(bridge) + i < weight1 :
            bridge.append(i)
            bridge.pop(0)
            count += 1
            print(bridge)
            print(sum(bridge))

        elif sum(bridge) + i >= weight1:
            bridge.append(0)
            bridge.pop(0)
            count += 1
            print(bridge)
            print(sum(bridge))


            # if sum(bridge) + i <= weight1:
            #     bridge.append(i)
            #     bridge.pop(0)
            #     count += 1
            #     print(bridge)
            #     print(sum(bridge))



print(count)