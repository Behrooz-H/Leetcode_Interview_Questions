"""
0408. Valid Word Abbreviation

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. 
The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.    
    """
    


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        # check for the edge cases

        i=j=0 # index for abbr array
        while j<len(word) and i<len(abbr):  # O(N)
            print('j={j}, i={i}, word[j]={word[j]}, abbr[i]={abbr[i]}')
            if abbr[i].isalpha(): 
                if word[j]!=abbr[i] :
                    return False    
                elif word[j]==abbr[i]:
                        i+=1
                        j+=1
            else:
                if abbr[i]=="0":
                    return False
                num=[]
                while i<len(abbr) and abbr[i].isnumeric():
                    num.append(abbr[i])
                    i+=1
                step=int("".join(num))
                print("step={step}")
                j+=step
        return True if j== len(word) and  i== len(abbr) else False
                
"""
Time=O(N)
Space=O(1)"""