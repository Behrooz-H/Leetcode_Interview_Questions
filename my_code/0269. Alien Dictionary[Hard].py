"""
269. Alien Dictionary
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.
You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.
If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".
Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d: 
                    reverse_adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): 
                    return ""

        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result: 
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)
    
"""
Time complexity : O(C).
Building the adjacency list has a time complexity of O(C) for the same reason as in Approach 1.
Again, like in Approach 1, we traverse every "edge", but this time we're using depth-first-search.
Let N be the total number of strings in the input list.
Let C be the total length of all the words in the input list, added together.
Let U be the total number of unique letters in the alien alphabet. 
While this is limited to 26 in the question description, we'll still look at how it would impact the complexity if it was not limited (as this could potentially be a follow-up question).


Space complexity : O(1) or O(U+min(U^2,N)).
Like in Approach 1, we build an adjacency list. Even though this one is a reversed adjacency list, it still contains the same number of relations
            """