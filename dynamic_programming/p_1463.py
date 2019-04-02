#1 -> 0
#2 -> 1
#3 -> 1

#4 -> #2 -> 2
#5 -> #4 -> #2 -> 3

x = int(input())

dynamic_list = {1:0}

def return_minimum(target ,dynamic_list):
    possible_list = []
    if target%3 == 0:
        possible_list.append(dynamic_list[target/3])

    if target%2 ==0:
        possible_list.append(dynamic_list[target/2])

    possible_list.append(dynamic_list[target-1])

    return min(possible_list) + 1

for i in range(2,x+1):
    temp = return_minimum(i, dynamic_list)
    dynamic_list[i] = temp
    # print(temp)

print(dynamic_list[x])
