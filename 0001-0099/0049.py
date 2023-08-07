"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in d:
                d[sort_s].append(s)
            else:
                d[sort_s] = [s]
        return list(d.values())
