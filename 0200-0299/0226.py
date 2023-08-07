"""
Given the root of a binary tree, invert the tree horizontally, and return its root.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if root.left is not None:
                invert(root.left)
            if root.right is not None:
                invert(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

        if root is not None:
            invert(root)
        return root
