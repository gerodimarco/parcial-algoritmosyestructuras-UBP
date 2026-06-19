from graphs.graph import Graph


def main():

    print("=" * 50)
    print("DEMO - GRAFOS")
    print("=" * 50)

    graph = Graph()

    # Red de rutas simulada
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    graph.add_edge("C", "E", 3)
    graph.add_edge("D", "F", 2)
    graph.add_edge("E", "F", 4)

    print("\n--- BFS desde A ---")
    print(graph.bfs("A"))

    print("\n--- DFS desde A ---")
    print(graph.dfs("A"))

    print("\n--- Dijkstra desde A ---")

    distances = graph.dijkstra("A")

    for node, distance in distances.items():
        print(f"{node}: {distance}")

    print("\n--- Kruskal (Árbol de expansión mínima) ---")

    mst, total_cost = graph.kruskal()

    for source, destination, weight in mst:
        print(
            f"{source} -> {destination} "
            f"(costo={weight})"
        )

    print(f"\nCosto total MST: {total_cost}")


if __name__ == "__main__":
    main()