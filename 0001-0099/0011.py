"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(left_i, right_i):
            return min(height[left_i], height[right_i]) * (right_i - left_i)

        left_i = 0
        right_i = len(height) - 1
        left_max = height[left_i]
        right_max = height[right_i]
        max_area = area(left_i, right_i)
        while right_i - left_i > 1:
            if left_max < right_max:
                left_i += 1
                if height[left_i] > left_max:
                    left_max = height[left_i]
                    max_area = max(max_area, area(left_i, right_i))
                    continue
            else:
                right_i -= 1
                if height[right_i] > right_max:
                    right_max = height[right_i]
                    max_area = max(max_area, area(left_i, right_i))
                    continue
        return max_area
