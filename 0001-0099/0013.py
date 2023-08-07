"""
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        val = 0
        # iterate through characters in string
        while i < len(s):
            # if / else for each possible char
            c = s[i]
            if c == "I":
                # look ahead one to see if we need to subtract
                if i + 1 < len(s):
                    if s[i + 1] == "V":
                        val = val + 4
                        # if we do, make sure you change the iteration number to skip that next char
                        i = i + 1
                    elif s[i + 1] == "X":
                        val = val + 9
                        i = i + 1
                    else:
                        val = val + 1
                else:
                    val = val + 1
            elif c == "V":
                val = val + 5
            elif c == "X":
                if i + 1 < len(s):
                    if s[i + 1] == "L":
                        val = val + 40
                        i = i + 1
                    elif s[i + 1] == "C":
                        val = val + 90
                        i = i + 1
                    else:
                        val = val + 10
                else:
                    val = val + 10
            elif c == "L":
                val = val + 50
            elif c == "C":
                if i + 1 < len(s):
                    if s[i + 1] == "D":
                        val = val + 400
                        i = i + 1
                    elif s[i + 1] == "M":
                        val = val + 900
                        i = i + 1
                    else:
                        val = val + 100
                else:
                    val = val + 100
            elif c == "D":
                val = val + 500
            elif c == "M":
                val = val + 1000

            i = i + 1
        return val
