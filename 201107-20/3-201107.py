class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        l = []

        dic = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for ch in s:
            if ch in dic:
                if not l or l[-1] != dic[ch]:
                    return False
                l.pop()
            else:
                l.append(ch)

        return not l
