from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            length = right - left
            if height[left] < height[right]:
                min_height = height[left]
                left += 1
            else:
                min_height = height[right]
                right -= 1

            area = length * min_height
            max_area = max(area, max_area)

        return max_area


res = Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res)
