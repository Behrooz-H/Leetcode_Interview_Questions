"""
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


# Time complexity: O(4^N *N) where N is the length of digits. Note that 4 in this expression is referring to
# the maximum value length in the hash map, and not to the length of the input.

# Backtracking
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations




class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dct={"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"],
             "6":["m","n","o"], "7" :["p","q", "r", "s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        res = []
        for num in digits:
            if not res:
                res=dct[num].copy()
            else:
                ans = []
                while res:
                    el=res.pop(0)
                    for val in dct[num]:
                        ans.append(el+val)
                res=ans
        return res


if __name__=="__main__":
    sol=Solution2()
    sol.letterCombinations("22")
