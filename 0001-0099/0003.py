"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        substr_max_len = 0
        for i in range(0, len(s)):
            substr_len = 0
            chars = set()
            found_dupe = False
            for j in range(i, len(s)):
                if s[j] in chars:
                    found_dupe = True
                    if substr_len > substr_max_len:
                        substr_max_len = substr_len
                    break
                else:
                    chars.add(s[j])
                    substr_len = substr_len + 1
            if not found_dupe and substr_max_len < substr_len:
                substr_max_len = substr_len
        return substr_max_len
