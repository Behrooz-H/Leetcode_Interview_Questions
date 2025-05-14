"""
Next Largest Number to the Right [Stack Solution]  

Given an  integer array  nums.  return an  output array res where,  
for each  value  nums[i], res[i] is the first number to the right that's larger than nums[i]. 
If no larger number exists to the right of nums [i J, set res [i] to -1.   

"""

def next_largest_number_to_the_right(nums:List(int)):
    res , stack =[0]*len(nums), []
    for index in range(len(nums), -1, -1):
        while stack and stack[-1]<=nums[index]:
            stack.pop(-1)
        res[index] = -1 if not stack  else stack[-1]
        stack.append(nums(i))
    return res

# Time O(N) for the loop
# Space O(N) for the stack