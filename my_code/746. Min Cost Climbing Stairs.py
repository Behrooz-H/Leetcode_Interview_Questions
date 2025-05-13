"""
746. Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2 = cost[0] if len(cost)>0 else 0 ,cost[1] if len(cost)>1 else 0
        for i in range(2,len(cost)):
            current = cost[i] + min(dp1, dp2)
            dp1,dp2=dp2,current
        return min(dp1, dp2)



class Week_solution:
    dct ={}
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(cost):
            if len(cost)<=0:
                return 0
            if len(cost)==1:
                return cost[0]
            if len(cost)==2:
                return cost[-1]
            if (len(cost) - 2) not in self.dct:
                self.dct[len(cost) - 2]= dfs(cost[:-2])
            if (len(cost) - 1) not in self.dct:
                self.dct[len(cost) - 1]= dfs(cost[:-1])
            self.dct[len(cost)]= cost[-1]+min(self.dct[len(cost)-2],self.dct[len(cost)-1])
            return self.dct[len(cost)]
        return dfs(cost+[0])

if __name__=="__main__":
    sol=Solution()
    print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
    Week_solution =Week_solution()
    print(Week_solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
    # print(Week_solution.minCostClimbingStairs([10,15,20]))
"""
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size(), 0);
        dp[0] = cost[0], dp[1] = cost[1];
        
        // cout << dp[0] << " " << dp[1] << " ";
        for(int i = 2; i < cost.size(); ++i){
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]);
            // cout << dp[i] << " ";
        }
        // cout << endl;
        return min(dp[cost.size() - 1], dp[cost.size() - 2]);
    }
};
"""
