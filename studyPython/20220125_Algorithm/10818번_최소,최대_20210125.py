import sys

count = int(sys.stdin.readline())
numbers = sys.stdin.readline()
nums = numbers.split(" ")

li = []

# maximum, minimum = -10000000000, 10000000000
#
# for n in nums:
#
#     if maximum < int(n) :
#         maximum = int(n)
#     if minimum > int(n) :
#         minimum = int(n)
#
# print(minimum, maximum)

for n in nums:
    li.append(int(n))

minimum, maximum = min(li), max(li)

print(minimum, maximum)