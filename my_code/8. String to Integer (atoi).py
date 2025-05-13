"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""



# Time complexity: O(N)
# We visit each character in the input at most once and for each character we spend a constant amount of time.
#
# Space complexity: O(1)
# We have used only constant space to store the sign and the result.

class Solution:
    class Solution:

        def myAtoi(self, s: str) -> int:
            def check(temp_res: int):
                if temp_res > (2 ** 31) - 1:
                    return (2 ** 31) - 1
                elif temp_res < (-2 ** 31):
                    return (-2 ** 31)
                else:
                    return temp_res

            s = s.strip()
            if len(s) == 0:
                return 0
            flag = -1 if s[0] == "-" else 1
            s = s[1:] if (s[0] == "-" or s[0] == "+") else s
            res = 0
            for i in s:
                if "0" <= i <= "9":
                    res *= 10
                    res += int(i)
                    res = flag * check(flag * res)
                else:
                    break
            return check(flag * res)


class Weeker_solution:

    def myAtoi(self, s: str) -> int:
        def check(temp_res: int):
            if temp_res > (2 ** 31) - 1:
                return (2 ** 31) - 1
            elif temp_res < (-2 ** 31):
                return -2 ** 31
            else:
                return temp_res

        s = s.strip()
        if len(s) == 0:
            return 0
        flag = -1 if s[0] == "-" else 1
        s = s[1:] if (s[0] == "-" or s[0] == "+") else s
        res = "0"
        for i in s:
            if "0" <= i <= "9":
                res += int(i)
            else:
                break
        return check(flag* int(res))


if __name__=="__main__":
    sol=Solution()
    sol.myAtoi("   -42")
