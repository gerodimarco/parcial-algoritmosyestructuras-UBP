from advanced_algorithms.pattern_matching import (
    brute_force_search,
    kmp_search
)

import timeit


def main():

    print("=" * 50)
    print("DEMO - BUSQUEDA DE PATRONES")
    print("=" * 50)

    text = (
        "Acceso no autorizado detectado "
        "en el servidor principal. "
        "Se registra acceso sospechoso "
        "desde una direccion externa."
    )

    pattern = "acceso"

    print("\nTexto:")
    print(text)

    print(f"\nPatron buscado: '{pattern}'")

    brute_result = brute_force_search(
        text.lower(),
        pattern.lower()
    )

    kmp_result = kmp_search(
        text.lower(),
        pattern.lower()
    )

    print("\nResultado Fuerza Bruta:")
    print(brute_result)

    print("\nResultado KMP:")
    print(kmp_result)

    brute_time = timeit.timeit(
        lambda: brute_force_search(
            text.lower(),
            pattern.lower()
        ),
        number=10000
    )

    kmp_time = timeit.timeit(
        lambda: kmp_search(
            text.lower(),
            pattern.lower()
        ),
        number=10000
    )

    print("\n--- TIEMPOS ---")

    print(
        f"Fuerza Bruta: "
        f"{brute_time:.6f} segundos"
    )

    print(
        f"KMP: "
        f"{kmp_time:.6f} segundos"
    )


if __name__ == "__main__":
    main()

    