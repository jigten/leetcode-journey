def myPow(x: float, n: int) -> float:
    def helper(x, n, res):
        if n == 0:
            return 1
        if n == 1:
            return res

        if n % 2 == 0:
            return helper(x, n // 2, helper(x, n // 2, res * x))

        return helper(x, (n - 1) // 2, helper(x, n // 2, res * x) * x)

    if n < 0:
        return helper(1 / x, -n, 1 / x)

    return helper(x, n, x)


if __name__ == "__main__":
    print(myPow(x=2.00000, n=10))
    print(myPow(x=2.10000, n=3))
    print(myPow(x=2.00000, n=-2))
    print(myPow(x=0.44528, n=0))
