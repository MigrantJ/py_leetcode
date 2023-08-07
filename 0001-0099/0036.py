"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import math

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                num = board[row_idx][col_idx]
                if num == ".":
                    continue

                if num in rows[row_idx]:
                    return False
                else:
                    rows[row_idx].add(num)

                if num in cols[col_idx]:
                    return False
                else:
                    cols[col_idx].add(num)

                box_idx = 3 * math.floor(row_idx / 3) + math.floor(col_idx / 3)
                if num in boxes[box_idx]:
                    return False
                else:
                    boxes[box_idx].add(num)

        return True
