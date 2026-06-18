from models.event import Event


class Index:
    """
    Índice hash para acceso rápido a eventos.

    Utiliza un diccionario de Python para
    asociar IDs de eventos con sus objetos.

    """

    def __init__(self):
        self._index = {}

    def insert(self, event: Event) -> None:
        """
        Inserta un evento en el índice.

        Args:
            event (Event): Evento a indexar.
        """
        self._index[event.event_id] = event

    def get(self, event_id: int) -> Event | None:
        """
        Recupera un evento por ID.

        Args:
            event_id (int): ID buscado.
        Returns:
            Event | None
        """
        return self._index.get(event_id)

    def remove(self, event_id: int) -> bool:
        """
        Elimina un evento del índice.

        Args:
            event_id (int): ID del evento.
        Returns:
            bool
        """
        if event_id in self._index:
            del self._index[event_id]
            return True

        return False

    def contains(self, event_id: int) -> bool:
        """
        Verifica si un ID existe.

        Args:
            event_id (int)
        Returns:
            bool
        """
        return event_id in self._index

    def size(self) -> int:
        """
        Cantidad de elementos indexados.

        Returns:
            int
        """
        return len(self._index)