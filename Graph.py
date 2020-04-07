from Vertex import *
from Edge import *


class Graph:
    def __init__(self, arr):
        self.vertices = []
        self.edges = []
        for edge in arr:
            self.create_edge(edge[0], edge[1], edge[2])

    def create_edge(self, tail_nr, head_nr, length):
        tail = self.get_vertex(tail_nr)
        head = self.get_vertex(head_nr)
        if not tail:
            tail = self.create_vertex(tail_nr)
        if not head:
            head = self.create_vertex(head_nr)
        new_edge = Edge(tail, head, length)
        tail.add_edge(new_edge)
        head.add_edge(new_edge)
        self.edges.append(new_edge)

    def create_vertex(self, nr):
        new_vertex = Vertex(nr)
        self.vertices.append(new_vertex)
        return new_vertex

    def get_vertex(self, vertex_nr):
        for vertex in self.vertices:
            if vertex.get_number() == vertex_nr:
                return vertex

    def get_number_of_vertices(self):
        return len(self.vertices)

    def reset_vertices(self):
        for vertex in self.vertices:
            vertex.set_as_unexplored()

    def get_edge(self, tail, head):
        for edge in self.edges:
            if edge.get_tail() == tail and edge.get_head() == head:
                return edge


