"""
0340. Longest Substring with At Most K Distinct Characters
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

"""

import collections
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        max_size = 0
        counter = collections.Counter()
        
        left = 0
        for right in range(n):
            counter[s[right]] += 1
            
            while len(counter) > k: 
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            max_size = max(max_size, right - left + 1)
                    
        return max_size
    

"""
Time complexity: O(n)
In the iteration of the right boundary right, we shift it from 0 to n - 1. Although we may move the left boundary left in each step, 
left always stays to the left of right, which means left moves at most n - 1 times.
At each step, we update the value of an element in the hash map counter, which takes constant time.
To sum up, the overall time complexity is O(n).

Space complexity: O(k)
We need to record the occurrence of each distinct character in the valid window. During the iteration, there might be at most O(k+1)
unique characters in the window, which takes O(k) space."""






class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_size = 0
        counter = collections.Counter()
        
        for right in range(len(s)):
            counter[s[right]] += 1
            
            if len(counter) <= k:
                max_size += 1
            else:
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]

        return max_size