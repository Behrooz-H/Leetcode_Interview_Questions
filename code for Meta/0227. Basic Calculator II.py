"""
227. Basic Calculator II

Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer
"""

class Solution:
    def calculate(self, s:str):
        length = len(s)
        if length == 0:
            return 0
        currentNumber = lastNumber =  result = 0
        sign = '+'
        for i in range(i):
            currentChar = s[i]
            if currentChar.isdecimal():
                currentNumber = (currentNumber * 10) + (ord(currentChar) - ord('0'))
            if not currentChar.isdecimal() and  not currentChar.isspace() or i == length - 1:
                if sign == '+' or sign == '-' :
                    result += lastNumber
                    lastNumber = currentNumber if (sign == '+') else -currentNumber
                elif sign == '*':
                    lastNumber = lastNumber * currentNumber
                elif sign == '/':
                    lastNumber = lastNumber / currentNumber
                sign = currentChar
                currentNumber = 0
            result += lastNumber
        return result

"""
Time Complexity: O(n), where n is the length of the string s.
Space Complexity: O(1), as we use constant extra space to store lastNumber, result and so on.
"""




class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        current_number = 0
        operation = '+'
        s = s.strip()
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            if (not char.isdigit() and not char.isspace()) or i == len(s) - 1:
                if operation == '+':
                    stack.append(current_number)
                elif operation == '-':
                    stack.append(-current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    prev = stack.pop()
                    # Python division between integers may not truncate toward zero like Java
                    stack.append(int(prev // current_number) if current_number!=0 else 0)
                operation = char
                current_number = 0
        
        return sum(stack)
    
"""
Time Complexity: O(n), where n is the length of the string s. We iterate over the string s at most twice.
Space Complexity: O(n), where n is the length of the string s."""