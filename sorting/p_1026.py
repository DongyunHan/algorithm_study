# p_1026
# This problem itself is easy, but i should know the sorting algorithm itself.
# I just used built-in function.

num_var = int(input())

list_a = [int(ele) for ele in input().split()]
list_b = [int(ele) for ele in input().split()]

#print(list_a)
#print(list_b)

list_a.sort(reverse=True)
list_b.sort()

#print(list_a)
#print(list_b)

mul_val = 0
for ele_a, ele_b in zip(list_a,list_b):
    mul_val += ele_a*ele_b

print(mul_val)
