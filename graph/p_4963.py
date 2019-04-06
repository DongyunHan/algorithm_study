# p_4963
# need to be familiar with considering dfs/ bfs

def find_island(my_graph,w, h):
    num_find = 0
    stack_list = []

    # print(my_graph)
    # print("*" * 10)

    for i_x in range(w):
        for i_y in range(h):
            if my_graph[i_y][i_x] == 1:
                num_find +=1

                my_graph[i_y][i_x] = 0
                # print(my_graph)
                # print("*" * 10)
                stack_list.append((i_y,i_x))

                while stack_list:
                    loc_set = stack_list[0]
                    stack_list = stack_list[1:]

                    #explore up
                    if loc_set[0] > 0 and my_graph[loc_set[0]-1][loc_set[1]] == 1:
                        my_graph[loc_set[0]-1][loc_set[1]] = 0
                        stack_list.append((loc_set[0]-1, loc_set[1]))

                    #explore right
                    if loc_set[1] < w-1 and my_graph[loc_set[0]][loc_set[1] +1] == 1:
                        my_graph[loc_set[0]][loc_set[1] +1] = 0
                        stack_list.append((loc_set[0], loc_set[1] +1))


                    #explore left
                    if loc_set[1] > 0 and my_graph[loc_set[0]][loc_set[1] -1] == 1:
                        my_graph[loc_set[0]][loc_set[1] -1] = 0
                        stack_list.append((loc_set[0], loc_set[1] -1))

                    #explore down
                    if loc_set[0] < h-1  and my_graph[loc_set[0]+1][loc_set[1]] == 1:
                        my_graph[loc_set[0]+1][loc_set[1]] = 0
                        stack_list.append((loc_set[0]+1, loc_set[1]))

                    #explore diagonal right down
                    if loc_set[0] < h-1 and loc_set[1] <w-1 and my_graph[loc_set[0]+1][loc_set[1]+1] == 1:
                        my_graph[loc_set[0]+1][loc_set[1]+1] = 0
                        stack_list.append((loc_set[0]+1, loc_set[1]+1))

                    #explore diagonal left down
                    if loc_set[0] < h-1 and loc_set[1] > 0 and my_graph[loc_set[0]+1][loc_set[1]-1] == 1:
                        my_graph[loc_set[0]+1][loc_set[1]-1] = 0
                        stack_list.append((loc_set[0]+1, loc_set[1]-1))


                    #explore diagonal right up
                    if loc_set[0] > 0 and loc_set[1] < w-1 and my_graph[loc_set[0]-1][loc_set[1]+1] == 1:
                        my_graph[loc_set[0]-1][loc_set[1]+1] = 0
                        stack_list.append((loc_set[0]-1, loc_set[1]+1))

                    #explore diagonal left up
                    if loc_set[0] > 0 and loc_set[1] >0 and my_graph[loc_set[0]-1][loc_set[1]-1] == 1:
                        my_graph[loc_set[0]-1][loc_set[1]-1] = 0
                        stack_list.append((loc_set[0]-1, loc_set[1]-1))

    return num_find


while True:
    w, h = map(int, input().split())

    if w == h == 0:
        # print("stop")
        break;

    else:
        island_map = []
        for i in range(h):
            island_map.append([int(ele) for ele in input().split()])

        print(find_island(island_map, w, h))
