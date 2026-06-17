from dataclasses import dataclass


@dataclass
class Event:
    
    """
    Representa un incidente procesado por la plataforma.
    Attributes:
        event_id (int): Identificador único del evento.
        timestamp (str): Fecha y hora del incidente.
        category (str): Categoría del incidente.
        priority (int): Nivel de prioridad.
        text (str): Descripción del incidente.
        origin (str): Nodo de origen.
        destination (str): Nodo de destino.
    """

    event_id: int
    timestamp: str
    category: str
    priority: int
    text: str
    origin: str
    destination: str

    def __str__(self) -> str:
        return (
            f"Event("
            f"id={self.event_id}, "
            f"category='{self.category}', "
            f"priority={self.priority}, "
            f"origin='{self.origin}', "
            f"destination='{self.destination}')"
        )
    
