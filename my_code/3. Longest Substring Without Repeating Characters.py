"""
3. Longest Substring Without Repeating Characters

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = res = 0

        while right < len(s):
            
            index = chars[ord(s[right])]
            
            if index is not None and left <= index < right:  # This optimization is very important to skip the time when the old index is less than left and it reduces the left
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(s[right])] = right
            right += 1
        return res
    
    
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        left, max_len, observed= 0, 0 ,{}
        for right in range(0,len(s)):
            if s[right] in observed and observed[s[right]]>= left: # This optimization is very important to skip the time when the old index is less than left and it reduces the left
                    left = observed[s[right]]+1
            max_len = max(max_len, right-left+1)
            observed[s[right]]= right
        return max_len
    
    
    def lengthOfLongestSubstring_3(self, s: str) -> int:
        if not s:
            return 0
        left , right, max_length = 0,0,0
        visited={}
        while right<len(s):
            if s[right] in visited and visited[s[right]]<len(s)-1:
                    left=max(left,visited[s[right]]+1)
            visited[s[right]]=right
            max_length= max(max_length,right-left+1)
        
            right+=1
        return max_length

if __name__=="__main__":
    # strn=  "abcabcbb"
    # strn = "dvdf"
    strn= ""

    a=Solution()
    print(a.lengthOfLongestSubstring(strn))
