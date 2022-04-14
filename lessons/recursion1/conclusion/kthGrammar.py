def kthGrammar(n: int, k: int) -> int:
    if n == 1:
        return 0
    half = 2 ** (n - 2)
    if k <= half:
        return kthGrammar(n - 1, k)
    else:
        if kthGrammar(n - 1, k - half) == 0:
            return 1
        else:
            return 0


if __name__ == "__main__":
    print(kthGrammar(n=1, k=1))
    print(kthGrammar(n=2, k=1))
    print(kthGrammar(n=2, k=2))
