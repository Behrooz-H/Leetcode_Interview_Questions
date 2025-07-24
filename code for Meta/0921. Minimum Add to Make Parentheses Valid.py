
"""
921. Minimum Add to Make Parentheses Valid
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets
    
    
"""  
Time complexity: O(N)

We iterate over each character in the string s once. For each character, 
we either increment, decrement, or compare a counter. These operations take constant time. Therefore, the overall time complexity is linear, O(N).

Space complexity: O(1)

We use only two variables, openBrackets and minAddsRequired, to count unmatched brackets. 
These variables require constant space, and we do not use any extra data structures that depend on the input size. 
Thus, the space complexity is constant.
"""