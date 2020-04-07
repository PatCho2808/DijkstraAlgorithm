class Vertex:
    def __init__(self, number):
        self.number = number
        self.edges_to = []
        self.edges_from = []

    def get_number(self):
        return self.number

    def add_edge_to(self, edge):
        self.edges_to.append(edge)

    def add_edge_from(self, edge):
        self.edges_from.append(edge)

    def get_next_vertices(self):
        next_vertices = []
        for edge in self.edges_from:
            next_vertex = edge.get_head()
            next_vertices.append(next_vertex)
        return next_vertices

    def get_edges_from(self):
        return self.edges_from



