"""
1376. Time Needed to Inform All Employees

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee,
manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news.
He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e.,
After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.

"""
from typing import List
from collections import defaultdict

class Solution:
    @staticmethod
    def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dct = defaultdict(list)
        for index in range(len(manager)):  # making adjacency list
            dct[manager[index]].append(index)

        def dfs(pointer):
            if not dct[pointer]:
                return 0
            maxi=0
            for item in dct[pointer]:
                maxi = max(maxi, dfs(item))
            return maxi+informTime[pointer]
        return dfs(headID)
