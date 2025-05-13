"""
** Cutting Wood 

You are given an array representing the heights of trees, and an integer k representing the total length of wood that needs to be cut. 
For this task, a woodcutting machine is set to a  certain height, H. The machine cuts off the top part of all trees taller than H,  
while trees shorter than H  remain untouched.  Determine the highest possible setting of the woodcutter (H) so that it cuts at least k  meters of wood, Assume the woodcutter cannot be set higher than the height of the tallest tree in the array. 
"""
from typing import List

class Solution:
    def cutting_wood(self, heights:List[int], k:int)->int:
        def cuts_enough_wood(mid, k, heights):
            wood_collected = 0
            for height in heights:
                if height> mid:
                    wood_collected+=height
            return wood_collected >= k
            
        left , right= 0, max(heights)  # maximum of the heights will be binary searched
        while left<right:
            mid= (left+right)//2 + 1  # One index higher, will bias the mid point one pointer to the right
            if cuts_enough_wood(mid, k , heights):
                left=mid
            else:
                right=mid-1
        return right
    
        
        
        """ 
Time = O(N log K) where N is the number of the inouts in an array and k is the max of vlaue or the highest height
Space = O(1)    
    
        """