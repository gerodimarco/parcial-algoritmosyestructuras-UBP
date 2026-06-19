class AVLNode:
    """
    Nodo utilizado por el árbol AVL.
    Cada nodo almacena:

    - key: clave de búsqueda
    - value: objeto asociado
    - left: hijo izquierdo
    - right: hijo derecho
    - height: altura del nodo

    La altura es necesaria para mantener
    el balance del árbol AVL.
    """

    def __init__(self, key, value=None):
        self.key = key
        self.value = value

        self.left = None
        self.right = None

        self.height = 1

    def __str__(self):
        return f"AVLNode(key={self.key})"

    def __repr__(self):
        return self.__str__()