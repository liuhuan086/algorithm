from typing import List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         for i in range(nums.count(0)):
#             nums.remove(0)
#             nums.append(0)
#         print(nums)
#
#
# solution = Solution()
# solution.moveZeroes([0, 1, 0, 3, 12])


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                j += 1
        print(nums)


solution = Solution()
solution.moveZeroes([0, 1, 0, 3, 12])
