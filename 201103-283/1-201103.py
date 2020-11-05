from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if i != j:
                    nums[i] = 0
                    i += 1
                j += 1
        print(nums)


solution = Solution()
solution.moveZeroes([0, 1, 0, 3, 12])

"""
执行用时：
44 ms, 在所有 Python3 提交中击败了67.64%的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了5.03%的用户
"""
