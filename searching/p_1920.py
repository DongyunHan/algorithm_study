# p_1920
def binary_search(lookup_table, i):
    start = 0
    end = len(lookup_table)-1

    while start <= end:
        mid = (start + end)//2

        if(lookup_table[mid] == i):
            return 1
        elif lookup_table[mid] < i:
            start = mid +1
        else:
            end = mid -1

    return 0

num_a = input()
base_list = [int(ele) for ele in input().split()]

numb_b = input()
search_list = [int(ele) for ele in input().split()]

base_list.sort()

# print(base_list)
# print(search_list)

for i in search_list:
    print(binary_search(base_list, i))
