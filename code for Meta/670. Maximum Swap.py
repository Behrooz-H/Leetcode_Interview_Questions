""" 
670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        max_digit_index = -1
        swap_idx_1 = -1
        swap_idx_2 = -1

        # Traverse the string from right to left, tracking the max digit and
        # potential swap
        for i in range(n - 1, -1, -1):
            if max_digit_index == -1 or num_str[i] > num_str[max_digit_index]:
                max_digit_index = i  # Update the index of the max digit
            elif num_str[i] < num_str[max_digit_index]:
                swap_idx_1 = i  # Mark the smaller digit for swapping
                swap_idx_2 = (
                    max_digit_index  # Mark the larger digit for swapping
                )

        # Perform the swap if a valid swap is found
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = (
                num_str[swap_idx_2],
                num_str[swap_idx_1],
            )

        return int(
            "".join(num_str)
        )  # Return the new number or the original if no
        # swap occurred
        
        
        
""" 
Time complexity: O(n)
Converting the integer num to its string representation takes O(n).
The loop iterates over the string once from right to left, performing constant-time operations for each character, making the loop cost O(n).
Swap runs in constant time O(1).
Converting the modified string back to an integer takes O(n) time.
Thus, the overall time complexity is dominated by the traversal and conversions, giving us O(n).


Space complexity: O(n)
The numStr variable is a string representation of the input number, which requires O(n) space to store.
The other variables (maxDigitIndex, swapIdx1, swapIdx2) require O(1) space since they are just integer indices.
Therefore, the overall space complexity is O(n), mainly due to the string representation of the number.
"""