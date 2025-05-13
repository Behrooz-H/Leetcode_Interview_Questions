"""

14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""



from typing import List
#  Quick search or Binary search
# find the shortest string and from half of the length of taht begin comparison

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs, key=len))
        l, r, ans = 0, min_len, 0

        def valid(end):
            for s in strs:
                if s[:end] != strs[0][:end]:
                    return False
            return True

        while l <= r:
            mid = l + (r - l) // 2
            if valid(mid):
                l = mid + 1
                ans = mid
            else:
                r = mid - 1
        return strs[0][:ans]




class Quick_search_solution:
    def longestCommonPrefix(Self, strs):
        def isCommonPrefix(strs,length):
            str1 = strs[0][0, length]
            for i in range(len(strs)):
                if not strs[i].startswith(str1):
                    return False
            return True
        if not strs or len(strs) == 0 :
            return ""
        minlen =min(map(lambda x:len(x),strs))
        low,high = 1,minlen
        while low <= high:
            middle = (low + high) // 2
            if isCommonPrefix(strs, middle):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0].substring(0, (low + high) / 2)









# O (s)*N where N is the count of words and s is the length of the shortest word
class Week_solution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        res, i, flag = "", 0, True
        l = len(strs[0])
        if l == 0:
            return res
        while True:
            for s in strs:
                if i < l and i < len(s) and s[i] == strs[0][i]:
                    continue
                else:
                    return res
            res += strs[0][i]
            i += 1


