from advanced_structures.avl_node import AVLNode


class AVLTree:
    """
    Implementación de un Árbol AVL.
    Un AVL es un árbol binario de búsqueda
    auto-balanceado.

    Garantiza:

        Inserción -> O(log n)
        Búsqueda  -> O(log n)

    gracias a las rotaciones automáticas
    cuando el árbol pierde el balance.
    """

    def __init__(self):
        self.root = None

    # ==========================
    # ALTURA Y BALANCE
    # ==========================

    def _height(self, node):
        if node is None:
            return 0

        return node.height

    def _balance_factor(self, node):
        if node is None:
            return 0

        return (
            self._height(node.left)
            - self._height(node.right)
        )

    # ==========================
    # ROTACIONES
    # ==========================

    def _rotate_right(self, y):

        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = (
            1
            + max(
                self._height(y.left),
                self._height(y.right)
            )
        )

        x.height = (
            1
            + max(
                self._height(x.left),
                self._height(x.right)
            )
        )

        return x

    def _rotate_left(self, x):

        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = (
            1
            + max(
                self._height(x.left),
                self._height(x.right)
            )
        )

        y.height = (
            1
            + max(
                self._height(y.left),
                self._height(y.right)
            )
        )

        return y

    # ==========================
    # INSERCIÓN
    # ==========================

    def insert(self, key, value=None):
        self.root = self._insert(
            self.root,
            key,
            value
        )

    def _insert(
        self,
        node,
        key,
        value
    ):

        if node is None:
            return AVLNode(
                key,
                value
            )

        if key < node.key:

            node.left = self._insert(
                node.left,
                key,
                value
            )

        elif key > node.key:

            node.right = self._insert(
                node.right,
                key,
                value
            )

        else:
            return node

        node.height = (
            1
            + max(
                self._height(node.left),
                self._height(node.right)
            )
        )

        balance = self._balance_factor(node)

        # Caso izquierda-izquierda

        if (
            balance > 1
            and key < node.left.key
        ):
            return self._rotate_right(node)

        # Caso derecha-derecha

        if (
            balance < -1
            and key > node.right.key
        ):
            return self._rotate_left(node)

        # Caso izquierda-derecha

        if (
            balance > 1
            and key > node.left.key
        ):
            node.left = self._rotate_left(
                node.left
            )

            return self._rotate_right(node)

        # Caso derecha-izquierda

        if (
            balance < -1
            and key < node.right.key
        ):
            node.right = self._rotate_right(
                node.right
            )

            return self._rotate_left(node)

        return node

    # ==========================
    # BÚSQUEDA
    # ==========================

    def search(self, key):
        return self._search(
            self.root,
            key
        )

    def _search(
        self,
        node,
        key
    ):

        if node is None:
            return None

        if key == node.key:
            return node.value

        if key < node.key:
            return self._search(
                node.left,
                key
            )

        return self._search(
            node.right,
            key
        )

    # ==========================
    # RECORRIDO
    # ==========================

    def inorder(self):

        result = []

        self._inorder(
            self.root,
            result
        )

        return result

    def _inorder(
        self,
        node,
        result
    ):

        if node is None:
            return

        self._inorder(
            node.left,
            result
        )

        result.append(node.key)

        self._inorder(
            node.right,
            result
        )