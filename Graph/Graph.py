class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    

    
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()

print("Testing add edge method")
my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_edge(1,2)
my_graph.print_graph()

graph1 = Graph()
graph1.add_vertex('A')
graph1.add_vertex('B')
graph1.add_vertex('C')
graph1.add_vertex('D')
graph1.add_edge('A','B')
graph1.add_edge('B','C')
graph1.add_edge('C','A')

graph1.print_graph()

print("Testing  remove_edge")
graph1.remove_edge('A','D')
graph1.print_graph()

#testing remove vertex
graph2 = Graph()
graph2.add_vertex('A')
graph2.add_vertex('B')
graph2.add_vertex('C')
graph2.add_vertex('D')
graph2.add_edge('A','B')
graph2.add_edge('A','C')
graph2.add_edge('A','D')
graph2.add_edge('B','D')
graph2.add_edge('C','D')
graph2.print_graph()

print("Testing remove vertex")
graph2.remove_vertex('D')
graph2.print_graph()


