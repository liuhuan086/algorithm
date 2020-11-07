from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # i + 1是因为不和i重复
            left, right = i + 1, len(nums) - 1
            sums = nums[i] + nums[left] + nums[right]

            while left < right:
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    res.append([nums[i], nums[left], nums[right]])
            return res
