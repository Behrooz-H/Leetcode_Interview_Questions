"""

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""



class Solution:

    def is_palind(self, s: str):
        l, r = 0, len(s) - 1
        while l < r:
            if l < len(s) and r > -1 and s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        if l >= r:
            return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if l <len(s) and r>-1 and s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l >= r:
            return True
        sl=s[l+1:r+1]
        sr = s[l:r]
        return True if self.is_palind(sl) or self.is_palind(sr) else False
        # return True if sl==sl[::-1] or sr==sr[::-1] else False


if __name__ == '__main__':
    strn = "ebcbbececabbacecbbcbe"
    a = Solution()
    a.validPalindrome(strn)
