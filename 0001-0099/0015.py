"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()

        for p1 in range(0, len(nums) - 2):
            if nums[p1] > 0:
                break
            for p3 in range(len(nums) - 1, 1, -1):
                if nums[p3] < 0 or p3 - p1 <= 1:
                    break

                target = (nums[p1] + nums[p3]) * -1
                p2 = (p1 + p3) // 2
                left_bound = p1
                right_bound = p3
                while left_bound < p2 and p2 < right_bound:
                    if nums[p2] == target:
                        results.add((nums[p1], nums[p2], nums[p3]))
                        break
                    elif nums[p2] < target:
                        left_bound = p2
                        p2 = (p2 + right_bound) // 2
                    else:
                        right_bound = p2
                        p2 = (left_bound + p2) // 2

        results = [list(result) for result in results]
        return results
