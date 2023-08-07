"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        sets = []

        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1

            if counts[n] > len(sets):
                sets.append({n})
            else:
                sets[counts[n] - 1].add(n)

        return_set: set[int] = set()
        i = len(sets) - 1
        while len(return_set) < k:
            return_set.update(sets[i])
            i = i - 1

        return list(return_set)
