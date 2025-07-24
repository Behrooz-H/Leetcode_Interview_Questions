"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part.
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1].
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1,
and if the quotient is strictly less than -231, then return -231.
"""
#  it has five approaches
# Approach 4: Adding Powers of Two with Bit-Shifting  Time Complexity: O(logn) , Space: O(1)
# Approach 5: Binary Long Division Time Complexity: O(logn) , Space: O(1)
class Solution4:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        HALF_MIN_INT = MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # In the first loop, we simply find the largest double of divisor
        # that fits into the dividend.
        # The >= is because we're working in negatives. In essence, that
        # piece of code is checking that we're still nearer to 0 than we
        # are to INT_MIN.
        highest_double = divisor
        highest_power_of_two = -1
        while highest_double >= HALF_MIN_INT and dividend <= highest_double + highest_double:
            highest_power_of_two += highest_power_of_two
            highest_double += highest_double

        # In the second loop, we work out which powers of two fit in, by
        # halving highest_double and highest_power_of_two repeatedly.
        # We can do this using bit shifting so that we don't break the
        # rules of the question :-)
        quotient = 0
        while dividend <= divisor:
            if dividend <= highest_double:
                quotient += highest_power_of_two
                dividend -= highest_double
            # We know that these are always even, so no need to worry about the
            # annoying "bit-shift-odd-negative-number" case.
            highest_power_of_two >>= 1
            highest_double >>= 1

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return quotient if negatives == 1 else -quotient




class Solution5:
    def divide(self, dividend: int, divisor: int) -> int:

        # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # We need to convert both numbers to negatives.
        # Also, we count the number of negatives signs.
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        # We want to find the largest doubling of the divisor in the negative 32-bit
        # integer range that could fit into the dividend.
        # Note if it would cause an overflow by being less than HALF_INT_MIN,
        # then we just stop as we know double it would not fit into INT_MIN anyway.
        max_bit = 0
        while divisor >= HALF_MIN_INT and divisor + divisor >= dividend:
            max_bit += 1
            divisor += divisor

        quotient = 0
        # We start from the biggest bit and shift our divisor to the right
        # until we can't shift it any further.
        for bit in range(max_bit, -1, -1):
            # If the divisor fits into the dividend, then we should set the current
            # bit to 1. We can do this by subtracting a 1 shifted by the appropriate
            # number of bits.
            if divisor >= dividend:
                quotient -= (1 << bit)
                # Remove the current divisor from the dividend, as we've now
                # considered this part of it.
                dividend -= divisor
            # Shift the divisor to the right so that it's in the right place
            # for the next positon we're checking at.
            divisor = (divisor + 1) >> 1

        # If there was originally one negative sign, then
        # the quotient remains negative. Otherwise, switch
        # it to positive.
        return -quotient if negatives != 1 else quotient
