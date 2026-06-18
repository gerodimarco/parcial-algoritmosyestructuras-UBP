import heapq


class PriorityQueue:
    """
    Cola de prioridad basada en heap.

    Los eventos con menor valor de prioridad
    serán atendidos primero.
    """

    def __init__(self):
        self._heap = []

    def push(self, event):
        """
        Inserta un evento en la cola de prioridad.
        """
        heapq.heappush(
            self._heap,
            (
                event.priority,
                event.timestamp,
                event
            )
        )

    def pop(self):
        """
        Retorna el evento más prioritario.
        """
        if self.is_empty():
            return None

        return heapq.heappop(self._heap)[2]

    def peek(self):
        """
        Visualiza el siguiente evento.
        """
        if self.is_empty():
            return None

        return self._heap[0][2]

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)