import timeit

from advanced_algorithms.pattern_matching import (
    brute_force_search,
    kmp_search
)

from advanced_structures.avl_tree import AVLTree


def benchmark_pattern_matching():

    print("=" * 50)
    print("BENCHMARK - PATRON MATCHING")
    print("=" * 50)

    text = (
        "acceso_no_autorizado_"
        * 1000
    )

    pattern = "autorizado"

    brute_time = timeit.timeit(
        lambda: brute_force_search(
            text,
            pattern
        ),
        number=1000
    )

    kmp_time = timeit.timeit(
        lambda: kmp_search(
            text,
            pattern
        ),
        number=1000
    )

    print(
        f"Fuerza Bruta: "
        f"{brute_time:.6f} segundos"
    )

    print(
        f"KMP: "
        f"{kmp_time:.6f} segundos"
    )


def benchmark_avl():

    print("\n" + "=" * 50)
    print("BENCHMARK - AVL TREE")
    print("=" * 50)

    avl = AVLTree()

    for i in range(10000):
        avl.insert(i)

    search_time = timeit.timeit(
        lambda: avl.search(9999),
        number=10000
    )

    print(
        f"Busqueda AVL: "
        f"{search_time:.6f} segundos"
    )


def main():

    benchmark_pattern_matching()

    benchmark_avl()


if __name__ == "__main__":
    main()
    