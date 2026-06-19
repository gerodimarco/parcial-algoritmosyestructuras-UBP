from bisect import bisect_left


def linear_search(events, target_id):
    """
    Realiza una búsqueda secuencial de un evento por ID.

    Complejidad:
        O(n)

    Args:
        events (list): Lista de eventos.
        target_id (int): ID buscado.
    Returns:
        Event | None
    """
    for event in events:
        if event.event_id == target_id:
            return event

    return None


def binary_search(sorted_ids, target_id):
    """
    Realiza búsqueda binaria utilizando bisect.

    La lista debe estar previamente ordenada.

    Complejidad:
        O(log n)

    Args:
        sorted_ids (list[int]): Lista ordenada de IDs.
        target_id (int): ID buscado.
    Returns:
        int | None
        Posición encontrada o None.
    """

    position = bisect_left(sorted_ids, target_id)

    if position < len(sorted_ids) and sorted_ids[position] == target_id:
        return position

    return None