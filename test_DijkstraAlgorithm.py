from unittest import TestCase
from Graph import Graph
from DijkstraAlgorithm import *


class TestDijkstraAlgorithm(TestCase):
    def test_shortest_path(self):
        graph = Graph([[1, 3, 1],
                       [3, 2, 1],
                       [3, 4, 4],
                       [2, 4, 2],
                       [1, 2, 3]])

        dijkstra = DijkstraAlgorithm(graph, graph.get_vertex(1))
        dijkstra.compute()

        self.assertEqual(1, dijkstra.get_shortest_path(graph.get_vertex(3)))
        self.assertEqual(2, dijkstra.get_shortest_path(graph.get_vertex(2)))
        self.assertEqual(4, dijkstra.get_shortest_path(graph.get_vertex(4)))

        graph = Graph([[1, 4, 5],
                       [1, 7, 1],
                       [6, 7, 7],
                       [4, 6, 8],
                       [4, 5, 20],
                       [6, 5, 4],
                       [5, 3, 7],
                       [3, 4, 3],
                       [2, 3, 1],
                       [2, 3, 1],
                       [4, 2, 9],
                       [1, 2, 6]])

        dijkstra = DijkstraAlgorithm(graph, graph.get_vertex(1))
        dijkstra.compute()

        self.assertEqual(17, dijkstra.get_shortest_path(graph.get_vertex(5)))
        self.assertEqual(1, dijkstra.get_shortest_path(graph.get_vertex(7)))
        self.assertEqual(7, dijkstra.get_shortest_path(graph.get_vertex(3)))

