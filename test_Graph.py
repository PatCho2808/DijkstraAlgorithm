from unittest import TestCase
from Graph import *


class TestGraph(TestCase):
    def test_create_graph(self):
        graph = Graph([[1, 2, 1],
                       [2, 3, 2]])

        self.assertEqual([graph.get_vertex(2)], graph.get_vertex(1).get_next_vertices())
        self.assertEqual([graph.get_vertex(3)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([], graph.get_vertex(3).get_next_vertices())

        self.assertEqual(1, graph.get_edge(graph.get_vertex(1), graph.get_vertex(2)).get_length())
        self.assertEqual(2, graph.get_edge(graph.get_vertex(2), graph.get_vertex(3)).get_length())

        graph = Graph([[1, 2, 5],
                       [2, 3, 15],
                       [3, 1, 4]])

        self.assertEqual([graph.get_vertex(2)], graph.get_vertex(1).get_next_vertices())
        self.assertEqual([graph.get_vertex(3)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([graph.get_vertex(1)], graph.get_vertex(3).get_next_vertices())

        self.assertEqual(5, graph.get_edge(graph.get_vertex(1), graph.get_vertex(2)).get_length())
        self.assertEqual(15, graph.get_edge(graph.get_vertex(2), graph.get_vertex(3)).get_length())

        graph = Graph([[1, 2, 1],
                       [1, 3, 35],
                       [2, 3, 12],
                       [3, 1, 2]])

        self.assertEqual([graph.get_vertex(2), graph.get_vertex(3)], graph.get_vertex(1).get_next_vertices())
        self.assertEqual([graph.get_vertex(3)], graph.get_vertex(2).get_next_vertices())
        self.assertEqual([graph.get_vertex(1)], graph.get_vertex(3).get_next_vertices())

        self.assertEqual(35, graph.get_edge(graph.get_vertex(1), graph.get_vertex(3)).get_length())
        self.assertEqual(2, graph.get_edge(graph.get_vertex(3), graph.get_vertex(1)).get_length())





