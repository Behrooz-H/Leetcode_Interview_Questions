"""
273. Integer to English Words

Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"
"""
# Best Solution
class Solution:
    # Dictionary to store words for numbers
    number_to_words_map = {
        1000000000: "Billion", 1000000: "Million", 1000: "Thousand",
        100: "Hundred", 90: "Ninety", 80: "Eighty", 70: "Seventy",
        60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty",
        20: "Twenty", 19: "Nineteen", 18: "Eighteen", 17: "Seventeen",
        16: "Sixteen", 15: "Fifteen", 14: "Fourteen", 13: "Thirteen",
        12: "Twelve", 11: "Eleven", 10: "Ten", 9: "Nine", 8: "Eight",
        7: "Seven", 6: "Six", 5: "Five", 4: "Four", 3: "Three",
        2: "Two", 1: "One"
    }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        for value, word in self.number_to_words_map.items():
            # Check if the number is greater than or equal to the current unit
            if num >= value:
                # Convert the quotient to words if the current unit is 100 or greater
                prefix = (self.numberToWords(num // value) + " ") if num >= 100 else ""

                # Get the word for the current unit
                unit = word

                # Convert the remainder to words if it's not zero
                suffix = "" if num % value == 0 else " " + self.numberToWords(num % value)

                return prefix + unit + suffix

        return ""
    
"""
Let K be the number of pairs in numberToWordsMap and N be the number.
Time complexity: O(K)
The time complexity is O(K) because the loop iterates through the pairs until it finds a match. This complexity is linear with respect to the number of pairs, which is constant in practice as the number of pairs is fixed.

Space complexity: O(log 10​ N)
O(log 10 N), mainly due to the recursion stack in the convert function. The space used is proportional to the number of recursive calls made.
        """
  
  
  
  
#--------------------------------------------------------------------
  
# Second Best Solution
class Solution:
    def numberToWords(self, num: int) -> str:
        # Handle the special case where the number is zero
        if num == 0:
            return "Zero"

        # Arrays to store words for single digits, tens, and thousands
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        # StringBuilder to accumulate the result
        result = ""
        group_index = 0

        # Process the number in chunks of 1000
        while num > 0:
            # Process the last three digits
            if num % 1000 != 0:
                group_result = ""
                part = num % 1000

                # Handle hundreds
                if part >= 100:
                    group_result += ones[part // 100] + " Hundred "
                    part %= 100

                # Handle tens and units
                if part >= 20:
                    group_result += tens[part // 10] + " "
                    part %= 10

                # Handle units
                if part > 0:
                    group_result += ones[part] + " "

                # Append the scale (thousand, million, billion) for the current group
                group_result += thousands[group_index] + " "
                # Insert the group result at the beginning of the final result
                result = group_result + result
            # Move to the next chunk of 1000
            num //= 1000
            group_index += 1

        return result.strip()
    
"""   
Let N be the number.
Time complexity: O(log 10 N)
O(log10 N), because the number is divided by 1000 in each iteration, making the number of iterations proportional to the number of chunks, which is logarithmic.

Space complexity: O(1)
O(1), constant space. The space used is independent of the number's size, as it involves only a few string builders and arrays.  
"""