"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product = [1] * length
        right_product = [1] * length
        result = []

        for i in range(1, length):
            # accumulates to the right, leftmost stays 1
            left_product[i] = left_product[i - 1] * nums[i - 1]
        for i in range(length - 2, -1, -1):
            # accumulates to the left, rightmost stays 1
            right_product[i] = right_product[i + 1] * nums[i + 1]

        for i in range(length):
            result.append(left_product[i] * right_product[i])

        return result
