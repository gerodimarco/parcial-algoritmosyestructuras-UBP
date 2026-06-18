from models.event import Event


class EventStore:
    """
    Almacena y administra los eventos del sistema.

    Utiliza una lista dinámica de Python para guardar
    los incidentes registrados.

    """

    def __init__(self):
        self._events = []

    def add_event(self, event: Event) -> None:
        """
        Agrega un evento al almacenamiento.

        Args:
            event (Event): Evento a almacenar.
        """
        self._events.append(event)

    def get_all_events(self) -> list[Event]:
        """
        Retorna todos los eventos almacenados.

        Returns:
            list[Event]: Lista completa de eventos.
        """
        return self._events

    def find_by_id(self, event_id: int) -> Event | None:
        """
        Busca un evento por su ID mediante búsqueda secuencial.

        Args:
            event_id (int): ID buscado.
        Returns:
            Event | None
        """
        for event in self._events:
            if event.event_id == event_id:
                return event

        return None

    def remove_by_id(self, event_id: int) -> bool:
        """
        Elimina un evento por ID.

        Args:
            event_id (int): ID del evento.
        Returns:
            bool: True si fue eliminado, False en caso contrario.
        """
        for i, event in enumerate(self._events):
            if event.event_id == event_id:
                del self._events[i]
                return True

        return False

    def count(self) -> int:
        """
        Devuelve la cantidad total de eventos.
        Returns:
            int
        """
        return len(self._events)