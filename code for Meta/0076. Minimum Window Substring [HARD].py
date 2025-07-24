"""
76. Minimum Window Substring [Hard]
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)  # Required characters and their counts
        window = defaultdict(int)

        have = 0
        res = [float("inf"), 0, 0]  # [window_length, left, right]
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            # Contract window while it's valid
            while have == len(need):
                # Update result
                if (right - left + 1) < res[0]:
                    res = [right - left + 1, left, right]

                # Pop from left of window
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res[1], res[2]
        return s[l:r+1] if res[0] != float("inf") else ""

    
"""    Time Complexity : O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings S and T. The complexity is same as the previous approach. 
But in certain cases where ∣filtered_S∣ <<< ∣S∣, the complexity would reduce because the number of iterations would be 2∗∣filtered_S∣+∣S∣+∣T∣.
Space Complexity : O(∣S∣+∣T∣)"""