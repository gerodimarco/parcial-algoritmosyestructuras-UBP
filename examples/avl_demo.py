from advanced_structures.avl_tree import AVLTree


def main():

    print("=" * 50)
    print("DEMO - AVL TREE")
    print("=" * 50)

    avl = AVLTree()

    values = [30, 20, 10, 40, 50]

    print("\nInsertando valores:")

    for value in values:
        print(f"Insertando {value}")
        avl.insert(value)

    print("\nRecorrido inorder:")
    print(avl.inorder())

    print("\nBusqueda:")

    key = 40

    result = avl.search(key)

    if result is not None:
        print(f"Clave {key} encontrada")
    else:
        print(f"Clave {key} NO encontrada")

    key = 99

    result = avl.search(key)

    if result is not None:
        print(f"Clave {key} encontrada")
    else:
        print(f"Clave {key} NO encontrada")


if __name__ == "__main__":
    main()