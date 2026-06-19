from collections import defaultdict
from collections import deque
import heapq


class Graph:
    """
    Grafo representado mediante lista de adyacencia.

    Permite modelar la red:

        origen -> destino

    de los incidentes del sistema.

    Algoritmos implementados:

    - BFS
    - DFS
    - Dijkstra
    - Kruskal
    """

    def __init__(self):

        self.graph = defaultdict(list)
        self.edges = []

    # ==================================
    # CREACIÓN DEL GRAFO
    # ==================================

    def add_edge(
        self,
        source,
        destination,
        weight=1
    ):

        self.graph[source].append(
            (destination, weight)
        )

        self.edges.append(
            (
                weight,
                source,
                destination
            )
        )

    # ==================================
    # BFS
    # ==================================

    def bfs(self, start):

        visited = set()

        queue = deque([start])

        result = []

        while queue:

            node = queue.popleft()

            if node not in visited:

                visited.add(node)

                result.append(node)

                for neighbor, _ in self.graph[node]:

                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

    # ==================================
    # DFS
    # ==================================

    def dfs(self, start):

        visited = set()

        result = []

        self._dfs_recursive(
            start,
            visited,
            result
        )

        return result

    def _dfs_recursive(
        self,
        node,
        visited,
        result
    ):

        visited.add(node)

        result.append(node)

        for neighbor, _ in self.graph[node]:

            if neighbor not in visited:

                self._dfs_recursive(
                    neighbor,
                    visited,
                    result
                )

    # ==================================
    # DIJKSTRA
    # ==================================

    def dijkstra(
        self,
        start
    ):

        distances = {
            node: float("inf")
            for node in self.graph
        }

        distances[start] = 0

        priority_queue = [
            (0, start)
        ]

        while priority_queue:

            current_distance, current_node = (
                heapq.heappop(
                    priority_queue
                )
            )

            if (
                current_distance
                > distances[current_node]
            ):
                continue

            for (
                neighbor,
                weight
            ) in self.graph[current_node]:

                distance = (
                    current_distance
                    + weight
                )

                if (
                    distance
                    < distances.get(
                        neighbor,
                        float("inf")
                    )
                ):

                    distances[neighbor] = distance

                    heapq.heappush(
                        priority_queue,
                        (
                            distance,
                            neighbor
                        )
                    )

        return distances

    # ==================================
    # KRUSKAL
    # ==================================

    def kruskal(self):

        parent = {}

        rank = {}

        def find(node):

            if parent[node] != node:

                parent[node] = find(
                    parent[node]
                )

            return parent[node]

        def union(node1, node2):

            root1 = find(node1)

            root2 = find(node2)

            if root1 == root2:
                return False

            if rank[root1] < rank[root2]:

                parent[root1] = root2

            elif rank[root1] > rank[root2]:

                parent[root2] = root1

            else:

                parent[root2] = root1

                rank[root1] += 1

            return True

        vertices = set()

        for (
            weight,
            source,
            destination
        ) in self.edges:

            vertices.add(source)
            vertices.add(destination)

        for vertex in vertices:

            parent[vertex] = vertex

            rank[vertex] = 0

        mst = []

        total_cost = 0

        for (
            weight,
            source,
            destination
        ) in sorted(self.edges):

            if union(
                source,
                destination
            ):

                mst.append(
                    (
                        source,
                        destination,
                        weight
                    )
                )

                total_cost += weight

        return mst, total_cost