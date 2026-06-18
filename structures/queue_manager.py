from collections import deque


class QueueManager:
    """
    Implementación de una cola FIFO utilizando deque.
        Proporciona métodos para encolar, desencolar, revisar el primer elemento, verificar si está vacía y obtener su tamaño.
    """

    def __init__(self):
        self._queue = deque()

    def enqueue(self, item):
        """
        Agrega un elemento al final de la cola.
        """
        self._queue.append(item)

    def dequeue(self):
        """
        Remueve y retorna el primer elemento.
        """
        if self.is_empty():
            return None

        return self._queue.popleft()

    def peek(self):
        """
        Retorna el primer elemento sin removerlo.
        """
        if self.is_empty():
            return None

        return self._queue[0]

    def is_empty(self):
        """
        Verifica si la cola está vacía.
        """
        return len(self._queue) == 0

    def size(self):
        """
        Devuelve la cantidad de elementos.
        """
        return len(self._queue)