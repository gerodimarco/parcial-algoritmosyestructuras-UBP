from models.event import Event
from structures.queue_manager import QueueManager
from structures.priority_queue import PriorityQueue
from storage.event_store import EventStore
from storage.index import Index


def main():

    print("=" * 50)
    print("PLATAFORMA DE ANALISIS DE INCIDENTES")
    print("=" * 50)

    store = EventStore()
    index = Index()
    queue = QueueManager()
    pq = PriorityQueue()

    eventos = [
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
        Event(
            3,
            "2025-01-01 10:10",
            "Hardware",
            3,
            "Disco lleno",
            "E",
            "F"
        ),
    ]

    for event in eventos:
        store.add_event(event)
        index.insert(event)
        queue.enqueue(event)
        pq.push(event)

    print(f"\nCantidad de eventos almacenados: {store.count()}")

    print("\n--- Busqueda mediante indice hash ---")
    print(index.get(2))

    print("\n--- Cola FIFO (primer evento ingresado) ---")
    print(queue.peek())

    print("\n--- Cola de prioridad (evento mas importante) ---")
    print(pq.peek())

    print("\nDemostracion finalizada correctamente.")


if __name__ == "__main__":
    main()