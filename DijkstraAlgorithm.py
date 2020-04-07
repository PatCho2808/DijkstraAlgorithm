class DijkstraAlgorithm:
    def __init__(self, graph, source_vertex):
        self.graph = graph
        self.source_vertex = source_vertex
        self.processed_vertices = [source_vertex]
        self.vertices_to_process = graph.get_vertices()[:]
        self.vertices_to_process.remove(source_vertex)
        self.shortest_distances = {source_vertex: 0}

    def compute(self):
        while len(self.vertices_to_process) > 0:
            selected_edge = None
            score = None
            for vertex in self.processed_vertices:
                for edge in vertex.get_edges_from():
                    if edge.get_head() in self.vertices_to_process:
                        new_score = self.shortest_distances[vertex] + edge.get_length()
                        if not score or new_score < score:
                            selected_edge = edge
                            score = new_score
            self.vertices_to_process.remove(selected_edge.get_head())
            self.processed_vertices.append(selected_edge.get_head())
            self.shortest_distances[selected_edge.get_head()] = score

    def get_shortest_path(self, vertex):
        return self.shortest_distances[vertex]
