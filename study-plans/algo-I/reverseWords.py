def reverseWords(s: str) -> str:
    res = ""
    for w in s.split():
        temp, l, r = list(w), 0, len(w) - 1
        while l < r:
            temp[l], temp[r] = temp[r], temp[l]
            l += 1
            r -= 1
        if not res:
            res += "".join(temp)
        else:
            res += " " +  "".join(temp)
    return res

print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))
