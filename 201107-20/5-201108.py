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

        for i in s:
            if i not in dic:
                res.append(i)
            else:
                if not res or res[-1] != dic[i]:
                    return False
                res.pop()

        return res is None


print(Solution().isValid('[][(){}]'))
