# p_11399
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

# [a,b,c,d,e ...] 이라는 리스트가 있다고 가정해보자.
# 그리고 i 차례 사람이  기다려야하는 시간은 i보다 앞 사람들 만큼 기다려야 한다.
# i+n의 사람도 마찬가지. 즉 sort를 통해서 값이 작은 사람들을 앞에 배치시켜줘야 한다.

num_wait= int(input())
wait_min_list = [int(ele) for ele in input().split()]

wait_min_list.sort()
wait_sum = 0

for i in range(len(wait_min_list)):
    wait_sum += sum(wait_min_list[:i+1])

'''
for i in range(1,len(wait_min_list)):
    wait_min_list[i] += wait_min_list[i-1]   

print(sum(wait_min_list))
'''

print(wait_sum)
