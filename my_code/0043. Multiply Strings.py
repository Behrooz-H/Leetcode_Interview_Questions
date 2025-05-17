"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

The Logic is 
   abc
X
   def
   ----
= f *c
+ f*b*10
+f*a*100
+e*10*c
+e*10*b*10
+e*10*a*100
always f is it self  and e*10 and d*100 
    c is it self and b *10 and a*100
    
Reverse it to make it easier for manipulation
"""


# use this if using carry is mandatory
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize answer as a string of zeros of length N.
        N = len(num1) + len(num2)
        answer = [0] * N

        # Reverse num1 and num2
        first_number = num1[::-1]
        second_number = num2[::-1]

        for place2, digit2 in enumerate(second_number):
            # For each digit in second_number multiply the digit by all digits in first_number.
            for place1, digit1 in enumerate(first_number):
                # The number of zeros from multiplying to digits depends on the place
                # of digit2 in second_number and the place of the digit1 in first_number.
                num_zeros = place1 + place2

                # The digit currently at position numZeros in the answer string
                # is carried over and summed with the current result.
                carry = answer[num_zeros]
                multiplication = int(digit1) * int(digit2) + carry

                # Set the ones place of the multiplication result.
                answer[num_zeros] = multiplication % 10

                # Carry the tens place of the multiplication result by
                # adding it to the next position in the answer array.
                answer[num_zeros + 1] += multiplication // 10

        # Pop the excess 0 from the end of answer.
        if answer[-1] == 0:
            answer.pop()

        return "".join(str(digit) for digit in reversed(answer))

"""
Time complexity: O(M⋅N).

During multiplication, we perform N operations for each of the M digits of the second number, so we need M⋅N time for it.

Space complexity: O(M+N).

The space used to store the output is not included in the space complexity. However, because strings are immutable in Python, Java, 
and Javascript, a temporary data structure, 
using O(M+N) space, is required to store the answer while it is updated.
"""


# Good Solution Since it does not use any direct int conv and converts one by oneuses conversion which is prohibited
sorted()
# Time O(M.N)
#Space O(M+N)