class Solution:
    def a(self, s: str) -> int:
        if not s:
            return 0
        left , right, max_length = 0,0,0
        visited={}
        while right<len(s) and left < len(s):
            if s[right] not in visited:
                visited[s[right]] = right
                print(f"left={left} and right={right}")
                max_length= max(max_length, right-left+1)
                right+=1
            else: 
                left=right
                right+=1
                visited={s[left]:left}
        return max_length
            

if __name__ =="__main__":
    s= "abcabcbb"
    sol=Solution()
    sol.a(s)