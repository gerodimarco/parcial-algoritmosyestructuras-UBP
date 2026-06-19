import random
import timeit

from models.event import Event

from algorithms.searching import (
    linear_search,
    binary_search
)

from algorithms.sorting import (
    insertion_sort,
    merge_sort
)


def benchmark_search():

    print("\nSEARCH BENCHMARK")
    print("-" * 60)

    for size in [100, 1000, 10000]:

        events = [
            Event(
                i,
                "2025-01-01",
                "Network",
                1,
                "Test",
                "A",
                "B"
            )
            for i in range(size)
        ]

        ids = list(range(size))

        target = size - 1

        linear_time = timeit.timeit(
            lambda: linear_search(events, target),
            number=1000
        )

        binary_time = timeit.timeit(
            lambda: binary_search(ids, target),
            number=1000
        )

        print(
            f"Size={size:<6}"
            f" Linear={linear_time:.6f}s"
            f" Binary={binary_time:.6f}s"
        )


def benchmark_sort():

    print("\nSORT BENCHMARK")
    print("-" * 60)

    for size in [100, 1000]:

        data = random.sample(
            range(size * 10),
            size
        )

        insertion_time = timeit.timeit(
            lambda: insertion_sort(data),
            number=10
        )

        merge_time = timeit.timeit(
            lambda: merge_sort(data),
            number=10
        )

        builtin_time = timeit.timeit(
            lambda: sorted(data),
            number=10
        )

        print(
            f"Size={size:<6}"
            f" Insertion={insertion_time:.6f}s"
            f" Merge={merge_time:.6f}s"
            f" Sorted={builtin_time:.6f}s"
        )


if __name__ == "__main__":

    benchmark_search()

    benchmark_sort()