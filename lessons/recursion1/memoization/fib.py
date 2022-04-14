from collections import defaultdict


def fib(n: int) -> int:
    cache = defaultdict(int)

    if n < 2:
        return n

    if n in cache:
        return cache[n]

    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


if __name__ == "__main__":
    print(fib(30))
