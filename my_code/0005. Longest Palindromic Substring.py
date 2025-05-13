"""
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

"""



# O(N**2) two loops
# Time complexity : O(n^2). Since expanding a palindrome around its center could take O(n)O(n) time,
# the overall complexity is O(n^2)O
# Space complexity : O(1)O(1).
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def grow_around(l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return r-l-1
        ans=""
        if not s or len(s)<2:
            return ans if not s else s if len(s)<2 else ""
        for i in range(len(s)):
            l1=grow_around(i,i)  # Odd occurrence count
            l2=grow_around(i,i+1)  # Even occurrence count
            l= max(l1, l2)
            ans = s[i-(l-1)//2:(i+l//2)+1] if len(ans)< l else ans
        return ans
