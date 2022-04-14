def mySqrt(x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (right + left) // 2
        val = mid * mid
        if val <= x < (mid + 1) * (mid + 1):
            return mid
        if val < x:
            left = mid + 1
        if val > x:
            right = mid


print(mySqrt(4))
print(mySqrt(8))
