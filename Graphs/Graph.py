class Graph: 
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
        
        return False
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2): 
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2): 
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except:
                pass
            return True
        return False
    
myGraph = Graph()
myGraph.add_vertex(1)
myGraph.add_vertex(2)
myGraph.add_vertex(3)
myGraph.add_vertex(4)

myGraph.add_edge(1, 2)
myGraph.add_edge(2, 3)
myGraph.add_edge(3, 1)

myGraph.remove_edge(1, 2)
myGraph.remove_edge(1, 4)

myGraph.print_graph()