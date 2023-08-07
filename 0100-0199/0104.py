"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recur(node, accum):
            if node is None:
                return accum
            accum += 1
            left = recur(node.left, accum)
            right = recur(node.right, accum)
            return left if left > right else right

        return recur(root, 0)