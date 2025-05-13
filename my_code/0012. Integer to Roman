"""
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


"""

class Solution:
    def intToRoman(self, num: int) -> str:
        m=num//1000
        num=num%1000
        m_9=num//900
        num=num%900
        d=num//500
        num=num%500
        d_4=num//400
        num=num%400
        c=num//100
        num=num%100
        c_9 = num//90
        num=num%90
        l=num//50
        num=num%50
        l_4=num//40
        num=num%40
        x=num//10
        num=num%10
        x_9=num//9
        num=num%9
        v=num//5
        num=num%5
        v_4=num//4
        num%=4
        return  m*"M"+m_9*"CM"+d*"D"+d_4*"CD"+c*"C"+c_9*"XC"+l*"L"+l_4*"XL"+x*"X"+x_9*"IX"+v*"V"+v_4*"IV"+num*"I"
