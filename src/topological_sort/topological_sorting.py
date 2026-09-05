from collections import defaultdict 

class Graph:
    def __init__(self,no_of_vertices):
        self.graph = defaultdict(list)
        self.no_vertices = no_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)


    def topological_sort_util(self, v,visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited,stack)
        stack.insert(0,v)
    
    def topological_sort(self):
        visited = []
        stack =  []
        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited,stack)
        print(stack)


cust_graph = Graph(8)
cust_graph.add_edge("A", "C")
cust_graph.add_edge("C", "E")
cust_graph.add_edge("E", "H")
cust_graph.add_edge("E", "F")
cust_graph.add_edge("F", "G")
cust_graph.add_edge("B", "D")
cust_graph.add_edge("B", "C")
cust_graph.add_edge("D", "F")
cust_graph.topological_sort()