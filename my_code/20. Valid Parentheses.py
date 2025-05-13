"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""


# Time complexity O(N)
# Space Complexity O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dct={"]":"[","}":"{",")":"("}
        for char in s:
            if char in dct.values():
                stack.append(char)
            elif not stack or dct[char]!=stack.pop():
                return False
        return False if stack else True
