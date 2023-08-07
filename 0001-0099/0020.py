"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = {"(", "{", "["}
        closes = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in opens:
                stack.append(c)
            elif c in closes:
                if len(stack) and closes[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
