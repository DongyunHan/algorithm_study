# bfs, dfs 에서
# Queue 또는 Stack을 활용하여 그래프를 traverse해야하는 예
# 1000 1 1000
# 999 1000

# 에러가 계속 났던 이유
# 답을 구하고 print 할 때,
# list 자체를 print해서 []를 포합하고 있었기 때문

class My_Vertex:
    def __init__(self, nodeA, nodeB=None):
        self.node_main = nodeA
        self.node_neighbors = []
        if nodeB != None:
            self.node_neighbors.append(nodeB)

    def put_neighbor(self, nodeB):
        self.node_neighbors.append(nodeB)

    def get_neighbors(self):
        self.node_neighbors.sort()
        return self.node_neighbors


class My_Graph:
    def __init__(self, num_ver, num_edge):
        self.num_ver = num_ver
        self.num_edge = num_edge
        self.vertex_set = {}

    def add_vertex(self, vertex1, vertex2):
        if vertex1 not in self.vertex_set:
            # print(str(vertex1) ,"is added")
            self.vertex_set[vertex1] = My_Vertex(vertex1, vertex2)
        else:
            # print(str(vertex1), "added anyway")
            self.get_vertex(vertex1).put_neighbor(vertex2)

    def get_vertex(self, vertex):
        return self.vertex_set[vertex]

    def get_neighbors(self, vertex):
        return self.get_vertex(vertex).get_neighbors()

    # def show_set(self):
    #     return (self.vertex_set)

    def bfs(self, start_v):
        visited_node = []
        temp_queue = [start_v]

        while temp_queue:
            from_vertex = temp_queue[0]
            temp_queue = temp_queue[1:]
            if from_vertex in visited_node:
                continue
            else:
                visited_node.append(from_vertex)

            temp_set = self.get_neighbors(from_vertex)
            temp_queue = temp_queue + temp_set

        return visited_node


        # while self.num_ver != len(visited_node):
        #     from_vertex = temp_queue[0]
        #     temp_queue = temp_queue[1:]
        #
        #     if from_vertex in visited_node:
        #         continue
        #     else:
        #         visited_node.append(from_vertex)
        #
        #     temp_set = self.get_neighbors(from_vertex)
        #     temp_queue = temp_queue + temp_set
        #
        # return visited_node

    def dfs(self, start_v):
        visited_node = []
        temp_stack = [start_v]

        while temp_stack:
            from_vertex = temp_stack[0]
            temp_stack = temp_stack[1:]

            if from_vertex in visited_node:
                continue
            else:
                visited_node.append(from_vertex)

            temp_set = self.get_neighbors(from_vertex)
            temp_stack = temp_set + temp_stack

        return visited_node
        # while self.num_ver != len(visited_node):
        #     from_vertex = temp_stack[0]
        #     temp_stack = temp_stack[1:]
        #
        #     if from_vertex in visited_node:
        #         continue
        #     else:
        #         visited_node.append(from_vertex)
        #
        #     temp_set = self.get_neighbors(from_vertex)
        #     temp_stack = temp_set + temp_stack
        #
        # return visited_node


def main():
    num_ver, num_edge, start_v = map(int, input().split())
    my_graph = My_Graph(num_ver, num_edge)

    for i in range(num_edge):
        nodeA, nodeB = map(int, input().split())
        my_graph.add_vertex(nodeA, nodeB)
        my_graph.add_vertex(nodeB, nodeA)

    print(' '.join(map(str,my_graph.dfs(start_v))))
    print(' '.join(map(str,my_graph.bfs(start_v))))


if __name__ == "__main__":
    main()
