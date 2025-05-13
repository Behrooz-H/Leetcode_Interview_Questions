"""
28. Find the Index of the First Occurrence in a String
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        for left in range(len(haystack)):
            right=0
            while right < len(haystack[left:]) and right < len(needle) and haystack[left:][right]==needle[right]:
                right+=1
            if right == len(needle):
                return left
        return -1
