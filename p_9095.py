#정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

case_num = int(input())
case_list = []

for i in range(case_num):
    case_list.append(int(input()))

max_value = max(case_list)

# value - number of ways
# 1 - 1
# 2 - (1,1), (2) -> 2
# 3 - (1,1,1), (1,2), (2,1), (3) -> 4

# 4 - case (4 -3 ) + case (4 - 2) + case (4-1)
#min_ways_list = {1:1, 2:2, 3:4}
min_ways_list = [0, 1, 2, 4]

for i in range(4, max_value+1):
    # print(i)
    # print(min_ways_list[-3:])
    # print("*"*5)
    min_ways_list.append(sum(min_ways_list[-3:]))


for i in case_list:
    print(min_ways_list[i])
