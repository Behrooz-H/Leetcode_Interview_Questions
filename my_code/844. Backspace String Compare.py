"""

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters
"""

"""BAD Solution

        i =max(len(s) , len(t))
        si,ti=0,0
        while i>0:
            if si < len(s):
                if s[si] == "#":
                    if si == 0:
                        s = s[1:]
                    elif len(s) > 2:
                        s = s[:si-1] + s[si+1:]
                        si-=1
                    elif len(s)<=2:
                        s=""
                else:
                    si+=1
            if ti < len(t):
                if t[ti] == "#":
                    if ti == 0:
                        t = t[1:]
                    elif len(t) > 2:
                        t = t[:ti-1] + t[ti+1:]
                        ti-=1
                    elif len(t) <= 2:
                        t = ""
                else:
                    ti += 1

            i -= 1
        return s == t
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ind_s, ind_t= len(s)-1 , len(t)-1
        counter = max(len(s) , len(t))
        while counter>0:
            s_count = 0
            t_count = 0
            while ind_s>=0 and s[ind_s]=="#":
                s_count+=1
                ind_s-=1
            while s_count>0:
                ind_s-=1
                if ind_s<0:
                    break
                if s[ind_s]!="#":
                    s_count-=1
                if s[ind_s] == "#":
                    s_count +=1

            while ind_t>=0 and t[ind_t] == "#":
                t_count+=1
                ind_t -= 1
            while t_count>0:
                ind_t -= 1
                if ind_t < 0:
                    break
                if t[ind_t] != "#":
                    t_count -= 1
                if t[ind_t] == "#":
                    t_count +=1
            if ind_s>-1 and ind_t>-1 and s[ind_s] != "#" and t[ind_t] != "#" and t[ind_t] != s[ind_s]:
                return False
            if ind_s>-1 and ind_t>-1 and s[ind_s]!="#" and t[ind_t]!="#" and t[ind_t]==s[ind_s]:
                ind_s -=1
                ind_t -=1
            counter -= 1
            if ind_s<0 and ind_t<0:
                return True
        if (ind_s>=0 and ind_t<0) or (ind_s<0 and ind_t>=0):
            return False
        return True


if __name__=="__main__":
    a=Solution()
    # s = "a##c"
    # t="#d#c"
    s="bxj##tw"
    t="bxo#j##tw"
    print(str(a.backspaceCompare(s,t)))
