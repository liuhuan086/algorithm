class Solution:
    def twoSum(self, nums, target):
        hash_dict = {}
        for i, j in enumerate(nums):
            if hash_dict.get(target - j) is not None:
                return [hash_dict.get(target - j), i]
            hash_dict[j] = i


res = Solution().twoSum([1, 2, 3, 4, 2, 5], 8)
print(res)
