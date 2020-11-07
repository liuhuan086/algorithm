class Solution:
    def twoSum(self, nums, target):
        hash_dic = {}
        for i, j in enumerate(nums):
            if hash_dic.get(target - j) is not None:
                return [hash_dic.get(target - j), i]
            hash_dic[i] = j
