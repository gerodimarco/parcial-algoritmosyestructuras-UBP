from graphs.graph import Graph

class Router:
    """
    Módulo de enrutamiento entre nodos.
    Utiliza el grafo de incidentes para
    calcular rutas óptimas.
    """
    def __init__(self):
        self._graph = Graph()

    def add_route(self, origin, destination, cost):
        self._graph.add_edge(origin, destination, cost)

    def shortest_path(self, origin, destination):
        distances = self._graph.dijkstra(origin)
        return distances.get(destination, float("inf"))
    
    