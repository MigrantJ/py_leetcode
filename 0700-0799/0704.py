"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # right is not inclusive!
        def recur(left: int, right: int):
            if right - left == 1:
                if nums[left] == target:
                    return left
                else:
                    return -1
            pivot = (right - left) // 2 + left
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                return recur(left, pivot)
            else:
                if pivot == len(nums) - 1:
                    return -1
                return recur(pivot + 1, right)

        return recur(0, len(nums))
