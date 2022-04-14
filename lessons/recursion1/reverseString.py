from typing import List


def reverseString(s: List[str]) -> None:
    # o(n) time | o(1) space
    # i, j = 0, len(s) - 1
    # while i < j:
    #     s[i], s[j] = s[j], s[i]
    #     i += 1
    #     j -= 1

    # recursion
    def helper(s, i, j):
        if i >= j:
            return
        s[i], s[j] = s[j], s[i]
        helper(s, i + 1, j - 1)

    helper(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    reverseString(s)
    print(s)
