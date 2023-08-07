"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        j = 0
        while True:
            try:
                char = strs[0][j]
                foundchar = True
                for i in range(1, len(strs)):
                    if strs[i][j] != char:
                        foundchar = False
                        break
                if not foundchar:
                    break
            except IndexError as e:
                break
            prefix += char
            j += 1
        return prefix
