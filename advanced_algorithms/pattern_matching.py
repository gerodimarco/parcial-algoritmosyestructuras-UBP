"""
Implementación de búsqueda de patrones.

Incluye:

- Fuerza Bruta
- KMP (Knuth-Morris-Pratt)

Aplicable al análisis de textos de incidentes.
"""


def brute_force_search(text, pattern):
    """
    Busca un patrón utilizando fuerza bruta.

    Retorna:
        índice de la primera coincidencia
        o -1 si no existe.
    """

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        match = True

        for j in range(m):

            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            return i

    return -1


def compute_lps(pattern):
    """
    Construye el arreglo LPS
    (Longest Prefix Suffix).

    Utilizado por KMP.
    """

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:

                length = lps[length - 1]

            else:

                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    Busca un patrón utilizando KMP.

    Retorna:
        índice de la primera coincidencia
        o -1 si no existe.
    """

    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    i = 0
    j = 0

    while i < n:

        if text[i] == pattern[j]:

            i += 1
            j += 1

        if j == m:
            return i - j

        elif i < n and text[i] != pattern[j]:

            if j != 0:

                j = lps[j - 1]

            else:

                i += 1

    return -1