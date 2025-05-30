"""
0161. One Edit Distance
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step
"""


class Solution:
    def isOneEditDistance(self, s: "str", t: "str") -> "bool":
        ns, nt = len(s), len(t)

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s) #? it is important find the shortest as the firsst argument

        # The strings are NOT one edit away from distance
        # if the length diff is more than 1.
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # If strings have the same length
                if ns == nt:
                    return s[i + 1 :] == t[i + 1 :]
                # If strings have different lengths
                else:
                    return s[i:] == t[i + 1 :]

        # If there are no diffs in ns distance
        # The strings are one edit away only if
        # t has one more character.
        return ns + 1 == nt
    
    
    
"""
Time complexity: O(N) in the worst case when string lengths are close enough abs(ns - nt) <= 1, where N is a number of characters in the longest string. O(1) in the best case when abs(ns - nt) > 1.
Space complexity: O(N) because strings are immutable in Python and Java and create substring costs O(N) space."""

