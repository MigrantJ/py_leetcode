"""
Given a string s, return the longest palindromic substring in s.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                substr = s[j : i + j]
                if substr == substr[::-1]:
                    return substr
        return ""
