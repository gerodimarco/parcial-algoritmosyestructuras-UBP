import random
import timeit

from algorithms.searching import linear_search
from algorithms.searching import binary_search

from algorithms.sorting import insertion_sort
from algorithms.sorting import merge_sort


def benchmark_search():

    print("\nSEARCH BENCHMARK")

    for size in [100, 1000, 10000]:

        data = list(range(size))

        target = size - 1

        linear_time = timeit.timeit(
            lambda: target in data,
            number=1000
        )

        binary_time = timeit.timeit(
            lambda: binary_search(data, target),
            number=1000
        )

        print(
            f"Size={size}"
            f" | Linear={linear_time:.6f}s"
            f" | Binary={binary_time:.6f}s"
        )


def benchmark_sort():

    print("\nSORT BENCHMARK")

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

        sorted_time = timeit.timeit(
            lambda: sorted(data),
            number=10
        )

        print(
            f"Size={size}"
            f" | Insertion={insertion_time:.6f}s"
            f" | Merge={merge_time:.6f}s"
            f" | Sorted={sorted_time:.6f}s"
        )


if __name__ == "__main__":

    benchmark_search()

    benchmark_sort()