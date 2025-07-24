""" 
556. Next Greater Element III
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

"""

def nextGreaterElement(n: int) -> int:
    digits = list(str(n))
    i = len(digits) - 2

    # Step 1: Find the first decreasing digit
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    # Step 2: Find the next larger digit from the right
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Step 3: Swap
    digits[i], digits[j] = digits[j], digits[i]

    # Step 4: Reverse the suffix
    digits[i + 1:] = reversed(digits[i + 1:])

    result = int(''.join(digits))
    return result if result < 2**31 else -1

"""
Time Complexity: O(k)

where k is the number of digits in n (since we traverse and reverse digits array).

Space Complexity: O(k)

for storing the digits as a list (due to string conversion and manipulation)."""