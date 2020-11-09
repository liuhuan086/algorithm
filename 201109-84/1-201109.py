from typing import List

"""
找出每根柱子的左边界，
用栈来保存柱子的高度，
栈底保存的最小的高度，
栈顶保存的最大的高度，（从小到大排列）
这样就说明第i个元素的左边界已经确定了（短板），
记录栈中每个元素的高度和它的下标（索引），
然后用每个元素（最左边界的高度）乘以该元素的下标（索引）一一进行对比，
求出最大值
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = 0
        if n > 0:
            for j in range(n):
                ans = max(ans, (right[j] - left[j] - 1) * heights[j])

        return ans


res = Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
print(res)
