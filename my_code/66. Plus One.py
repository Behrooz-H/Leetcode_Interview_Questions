"""
66. Plus One

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[(digits[-1] + 1) % 10]
        carry = (digits[-1] + 1) // 10
        for i in range(len(digits)-2,-1,-1):
            res.insert(0,((digits[i]+carry)%10))
            carry=(digits[i]+carry)//10
        if carry:
            res.insert(0,carry)
        return res
