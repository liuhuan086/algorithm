class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        dic = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        res = []

        for ch in s:
            if ch not in dic:
                res.append(ch)
            else:
                if not res or dic[ch] != res[-1]:
                    return False

                res.pop()

        return res is None
