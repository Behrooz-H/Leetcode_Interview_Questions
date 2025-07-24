"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
 
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
    
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0
        for right in range(len(s)):
            frequency_map[s[right]] = frequency_map.get(s[right], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[right]])

            # move the left pointer towards right if the current
            # window is invalid
            is_valid = (right + 1 - left - max_frequency <= k)
            if not is_valid:
                frequency_map[s[left]] -= 1
                left += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = right + 1 - left   # size of the sliding window never decreases

        return longest_substring_length
    
    
    """"
    Time Complexity O(n)
    Space Complexity O(m)->  m is the nmber of unique chars and if only lower case it will be 26 chars
    """