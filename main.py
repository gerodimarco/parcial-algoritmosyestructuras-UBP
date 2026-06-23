from models.event import Event
from storage.event_store import EventStore
from storage.index import Index
from structures.queue_manager import QueueManager
from structures.priority_queue import PriorityQueue

from advanced_structures.avl_tree import AVLTree
from graphs.graph import Graph
from advanced_algorithms.pattern_matching import kmp_search
from advanced_algorithms.rsa_demo import RSADemo


def main():

    print("=" * 60)
    print("PLATAFORMA DE ANALISIS DE INCIDENTES Y RUTAS")
    print("=" * 60)

    # =====================================
    # PARTE 1
    # =====================================

    print("\n[PARTE 1] Gestion de incidentes")

    store = EventStore()
    index = Index()
    queue = QueueManager()
    priority_queue = PriorityQueue()

    events = [
        Event(
            1,
            "2025-01-01 10:00",
            "Network",
            2,
            "Latencia alta",
            "A",
            "B"
        ),
        Event(
            2,
            "2025-01-01 10:05",
            "Security",
            1,
            "Acceso no autorizado",
            "C",
            "D"
        ),
    ]

    for event in events:

        store.add_event(event)

        index.insert(event)

        queue.enqueue(event)

        priority_queue.push(event)

    print("Eventos almacenados:", len(store.get_all_events()))
    print("Busqueda por ID:", index.get(2))

    # =====================================
    # AVL
    # =====================================

    print("\n[PARTE 2] AVL")

    avl = AVLTree()

    for value in [30, 20, 10, 40, 50]:
        avl.insert(value)

    print("Recorrido AVL:", avl.inorder())

    # =====================================
    # GRAFOS
    # =====================================

    print("\n[PARTE 2] Grafos")

    graph = Graph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("C", "D", 1)

    print("BFS:", graph.bfs("A"))

    # =====================================
    # KMP
    # =====================================

    print("\n[PARTE 2] Analisis de texto")

    text = "Acceso no autorizado detectado"

    result = kmp_search(
        text.lower(),
        "acceso"
    )

    print("Patron encontrado en posicion:", result)

    # =====================================
    # RSA
    # =====================================

    print("\n[PARTE 2] RSA")

    rsa = RSADemo()

    encrypted = rsa.encrypt("ALERTA")

    decrypted = rsa.decrypt(encrypted)

    print("Mensaje cifrado:", encrypted)

    print("Mensaje descifrado:", decrypted)

    print("\nSistema ejecutado correctamente.")


if __name__ == "__main__":
    main()

    