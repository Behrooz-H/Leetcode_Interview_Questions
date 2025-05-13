"""
38. Count and Say
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
"""


class Solution:
    def countAndSay(self, n):
        current_string = '1'
        for _ in range(n - 1):
            next_string = ''
            j = 0
            k = 0
            while j < len(current_string):
                while (k < len(current_string) and
                        current_string[k] == current_string[j]):
                    k += 1
                next_string += str(k - j) + current_string[j]
                j = k
            current_string = next_string
        return current_string



import re
class Solution:
    @staticmethod
    def countAndSay(n):
        s = '1'
        for _ in range(n - 1):
            # m.group(0) is the entire match, m.group(1) is its first digit
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s
