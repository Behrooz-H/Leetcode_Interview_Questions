"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        for c in s:
            if s.find(c)==s.rfind(c):
                return s.find(c)
        return -1
