"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


"""


class Solution1:
    def romanToInt(self, s: str) -> int:

        res, i = 0, 0
        map = {
            'I' : 1,
            'IV': 4,
            'V' : 5,
            'IX': 9,
            'X' : 10,
            'XL': 40,
            'L' : 50,
            'XC': 90,
            'C' : 100,
            'CD': 400,
            'D' : 500,
            'CM': 900,
            'M' : 1000
        }

        while i < len(s):
            if s[i:i + 2] in map:
                res += map[s[i:i + 2]]
                i += 2
            else:
                res += map[s[i]]
                i += 1

        return res


class Solution2(object):
    def romanToInt(self, s):
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res, i = 0, 0
        while i < len(s) - 1:
            if float(map[s[i]]) / map[s[i + 1]] == 0.2 or float(map[s[i]]) / map[s[i + 1]] == 0.1:
                res -= map[s[i]]
            else:
                res += map[s[i]]
            i += 1
        res += map[s[i]]

        return (res)


class Solution:
    def romanToInt(self, s: str) -> int:
        # create dictionary
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD",
                                                                                                                "CCCC").replace(
            "CM", "DCCCC")

        res = 0
        for c in s:
            res += values[c]

        return res


if __name__=="__main__":
    s1 = Solution1()
    s2 = Solution2()
    s="IIVXIDIVLLMCIV"
    print("s1:", s1.romanToInt(s))
    print("s2:", s2.romanToInt(s))
