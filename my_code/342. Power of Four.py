"""
342. Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

from math import sqrt, log


class Solution_third:
    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        return n > 0 and isinstance(log(n, 4),int)


class SolutionBest:
    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        return 0 < n == n & 1431655765 and not(n & (n - 1))


class Solution_second:
    def isPowerOfFour(self, n: int) -> bool:
        return 0 < n == int(sqrt(n)) * int(sqrt(n)) and not (n & (n - 1))
