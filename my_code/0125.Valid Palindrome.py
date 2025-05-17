"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s)-1
        while (left<right):
            while left<len(s) and not s[left].isalnum():
                left+=1
            while right>-1 and not s[right].isalnum():
                right-=1
            if right>-1 and left<len(s):
                if s[right].lower()!=s[left].lower():
                    return False
                else:
                    right-=1
                    left+=1
        return True


if __name__ == '__main__':
    strn=".;"
    a=Solution()
    a.isPalindrome(strn)


""" 
Time complexity : O(n), in length n of the string. We traverse over each character at-most once, until the two pointers meet in the middle, or when we break and return early.
Space complexity : O(1). No extra space required, at all.
"""