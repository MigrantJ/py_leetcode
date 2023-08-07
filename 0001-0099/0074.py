"""
You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        left = 0
        right = num_rows * num_cols

        while left < right:
            pivot = (right - left) // 2 + left
            pivot_row = pivot // num_cols
            pivot_col = pivot % num_cols
            candidate = matrix[pivot_row][pivot_col]

            if candidate > target:
                # look at left side of list
                right = pivot
            elif candidate < target:
                left = pivot + 1
            else:
                return True

        return False
