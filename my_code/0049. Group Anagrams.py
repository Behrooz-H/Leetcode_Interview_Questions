"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""
import collections
from typing import List


# Time Complexity : O(K*N) N is list element and k is the length of the longest string
# using the list of all chars and counting them instead of sorting the string will decrease the complexity

class Solution:
    def groupAnagrams(self,strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
"""
Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
Space Complexity: O(NK), the total information content stored in 
"""







# TIME Complexity: O (N*K*logK) because of the sort operation   where N is the length of strs, and K is the maximum length of a string in strs.
# The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(K \log K)O(KlogK) time.
class Second_Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = collections.defaultdict(list)
        for elem in strs:
            dct["".join(sorted(elem))].append(elem)
        return list(dct.values())
