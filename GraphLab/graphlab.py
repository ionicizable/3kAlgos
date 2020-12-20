import itertools

import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, matr: list):
        self.graph = matr

    @classmethod
    def init_by_adjacency_list(cls, list1):
        x = cls(list1)
        return x

    @classmethod
    def init_by_adjacency_matrix(cls, matrix):
        graph = [[]]
        for i in range(len(matrix) - 1):
            graph.append([])
        for i in range(len(matrix)):
            for j in range(i):
                if matrix[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)
        x = cls(graph)
        return x

    @classmethod
    def init_by_incendent_matrix(cls, matrix):
        graph = [[]]
        for i in range(len(matrix) - 1):
            graph.append([])
        for i in range(len(matrix[0])):
            cnt = []
            for j in range(len(matrix)):
                if matrix[j][i] == 1:
                    cnt.append(j)
            cnt1 = cnt.pop()
            cnt2 = cnt.pop()
            graph[cnt1].append(cnt2)
            graph[cnt2].append(cnt1)
        x = cls(graph)
        return x

    @classmethod
    def init_by_edges_list(cls, list_pairs: list):
        edges = 0
        graph = []
        for i in range(len(list_pairs)):
            if list_pairs[i][0] > edges:
                edges = list_pairs[i][0]
            if list_pairs[i][1] > edges:
                edges = list_pairs[i][1]
        edges += 1
        for i in range(edges):
            graph.append([])
        for i in range(len(list_pairs)):
            graph[list_pairs[i][0]].append(list_pairs[i][1])
            graph[list_pairs[i][1]].append(list_pairs[i][0])
        x = cls(graph)
        return x

    def add_arc(self, u: int, v: int):
        self.graph[u].append(v)

    def del_arc(self, u: int, v: int):
        self.graph[u].pop(v)

    def add_vertex(self):
        self.graph.append(len(self.graph))

    def del_vertex(self, vertex: int):
        self.graph.pop(vertex)

    def get_graph_by_adjacency_list(self):
        return self.graph

    def get_graph_by_adjacency_matrix(self):
        matr = []
        for i in range(len(self.graph)):
            matr.append([])
            for j in range(len(self.graph)):
                matr[i].append(0)

        for i in range(len(self.graph) - 1):
            for j in range(len(self.graph[i])):
                matr[i][self.graph[i][j]] = 1
                matr[self.graph[i][j]][i] = 1
        return matr

    def get_graph_by_incendent_matrix(self):
        matr = []
        for i in range(len(self.graph)):
            matr.append([])
            for j in range(len(self.graph)):
                matr[i].append(0)

        for i in range(len(self.graph)):
            for j in range(len(self.graph[i]) - 1):
                matr[i][self.graph[i][j]] = 1
        return matr

    def bfs(self, root):
        matrix = self.get_graph_by_adjacency_matrix()
        print("Broadth-first search")
        queue = [root]
        visited = []
        n = len(matrix)
        while queue:
            print("visited")
            print(visited)
            print("queue")
            print(queue)
            u = queue.pop(0)
            visited.append(u)
            for j in range(n):
                if matrix[u][j] == 1 and j not in visited and j not in queue:
                    queue.append(j)

    def get_graph_by_edges_list(self):
        matr = []
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                matr.append((i, self.graph[i][j]))
        return matr

    def get_graph(self):
        return self.graph

    def vertices_adjacent(self, a, b):
        if b in self.graph[a]:
            return True
        else:
            return False

    def find_independent_subsets(self):
        subsets = []
        for i in range(len(self.graph)):
            subsets.append(find_subsets(list(range(0, len(self.graph))), i))
        subsets.pop(0)
        print(subsets)
        independent_subsets = []
        for i in range(len(subsets)):
            for j in range(len(subsets[i])):
                flag = True
                for k in range(len(subsets[i][j])):
                    for v in range(len(subsets[i][j])):
                        if self.vertices_adjacent(subsets[i][j][k], subsets[i][j][v]):
                            flag = False
                if flag:
                    independent_subsets.append(subsets[i][j])
        print(independent_subsets)

    def __del__(self):
        print()


def find_subsets(s, n):
    return list(itertools.combinations(s, n))


def draw_graph(graph):
    G = nx.Graph()
    for i in range(len(graph) - 1):
        G.add_node(i)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            G.add_edge(i, graph[i][j])
    nx.draw_shell(G, nlist=[range(len(graph)), range(len(graph))], with_labels=True,
                  font_weight='bold', node_size=1200)


matrix = [[0, 1, 1, 1, 0],
          [1, 0, 1, 0, 0],
          [1, 1, 0, 0, 1],
          [1, 0, 0, 0, 0],
          [0, 0, 1, 0, 0]]

obj1 = Graph.init_by_adjacency_matrix(matrix)
draw_graph(obj1.get_graph())
plt.show()
obj1.bfs(0)
obj1.find_independent_subsets()
