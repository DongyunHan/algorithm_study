class My_Vertex:
    def __init__(self, nodeA, nodeB=None):
        self.node_main = nodeA
        self.node_neighbors = []
        if nodeB != None:
            self.node_neighbors.append(nodeB)

    def put_neighbor(self, nodeB):
        self.node_neighbors.append(nodeB)

    def get_neighbors(self):
        return self.node_neighbors


class My_Graph:
    def __init__(self, num_ver, num_edge):
        self.num_ver = num_ver
        self.num_edge = num_edge
        self.vertex_set = {}

    def add_vertex(self, vertex1, vertex2):
        if vertex1 not in self.vertex_set:
            print(str(vertex1) ,"is added")
            self.vertex_set[vertex1] = My_Vertex(vertex1, vertex2)
        else:
            print(str(vertex1), "added anyway")
            self.get_vertex(vertex1).put_neighbor(vertex2)

    def get_vertex(self, vertex):
        return self.vertex_set[vertex]

    def get_neighbors(self, vertex):
        return self.get_vertex(vertex).get_neighbors()

    # def show_set(self):
    #     return (self.vertex_set)

    def bfs(self, start_v):
        print("bfs")

    def dfs(self, start_v):
        print("dfs")


def main():
    num_ver, num_edge, start_v = map(int, input().split())
    my_graph = My_Graph(num_ver, num_edge)

    for i in range(num_edge):
        nodeA, nodeB = map(int, input().split())
        my_graph.add_vertex(nodeA, nodeB)
        my_graph.add_vertex(nodeB, nodeA)

    my_graph.bfs(start_v)
    my_graph.dfs(start_v)

    print(my_graph.get_vertex(1).get_neighbors())
    print(my_graph.get_vertex(2).get_neighbors())
    print(my_graph.get_vertex(3).get_neighbors())
    print(my_graph.get_vertex(4).get_neighbors())


if __name__ == "__main__":
    main()
