"""
06. Zigzag Conversion    
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);   
    """
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    curr_row = 0
    going_down = False

    for char in s:
        rows[curr_row] += char
        if curr_row == 0 or curr_row == numRows - 1:
            going_down = not going_down
        curr_row += 1 if going_down else -1

    return ''.join(rows)





""" 
Time Complexity: O(n)
where n = len(s) — each character is processed exactly once.


Space Complexity: O(n)
for storing characters in rows list.
"""