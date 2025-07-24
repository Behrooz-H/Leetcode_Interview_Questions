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
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True
    
"""    
    Given N as the length"" of s,

Time complexity: O(N).
The main while loop we use can iterate up to N / 2 times, since each iteration represents a pair of characters. On any given iteration, we may find a mismatch and call checkPalindrome twice. checkPalindrome can also iterate up to N / 2 times, in the worst case where the first and last character of s do not match.
Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means that checkPalindrome will never be called more than twice.
As such, we have a time complexity of O(N).

Space complexity: O(1).
The only extra space used is by the two pointers i and j, which can be considered constant relative to the input size.
"""    
    

class Solution2:

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
