"""
    0791. Custom Sort String
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.

 
    """
    
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dct={}
        result=""
        for char in s:  #O(N)
            dct[char]=dct.get(char,0)+1
            
        for letter in order: #O(M)
            result+=letter* dct.get(letter,0)
        
        if len(result)<len(s): #O(N-M)
            for el in s:
                if el not in result:
                    result+= el*dct[el ]
        return result
    
"""
        Time= O(n+m+(n-m)) = O(N)
        Space= O(N)
        """