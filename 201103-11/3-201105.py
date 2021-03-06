from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        max_area = 0
        right = len(height) - 1
        for i in range(len(height)):
            length = right - left
            if height[left] < height[right]:
                min_height = height[left]
                left += 1
            else:
                min_height = height[right]
                right -= 1
            area = length * min_height
            max_area = max(max_area, area)
        return max_area
