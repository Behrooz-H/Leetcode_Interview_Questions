"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Diredted Ascyclic Graph DAG is the graph which ha sno cycles and when

1- sort the graph node on the basis of their inputs pr inward edges (entering edges)
2- take the very smallest value ( the node with least enteries inside it)
3- using the adjucency list remove the node and all connected edges
"""
from typing import List
from collections import defaultdict

class Solution:

    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree=[0]*numCourses

       #Populate the graph and indegree
        for preq in prereq:
            graph[preq[1]].append(preq[0])
            indegree[preq[0]]+=1

        q=[]
        #to start from the  courses enter all the courses with 0 indegree to queue
        for i,ind in enumerate(indegree):
            if ind==0:
                q.append(i)

        cnt=0
        visited=set()
        #perform BFS
        while q:
            cur=q.pop(0)
            visited.add(cur)
            for neigh in graph[cur]:
                indegree[neigh]-=1
                #if indegree is 0 for the neighbour now, enqueue to queue
                if indegree[neigh]==0:
                    q.append(neigh)
        #check if all courses are taken or visited, if all are taken that means we were able to successfuly take all courses
        if len(visited)==numCourses:
            return True
        else:
            return False

if __name__=="__main__":
    sol = Solution()
    grid =[[0,1],[1,0]]
    sol.canFinish(2, grid)
















class Slow_solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dct = defaultdict(list)
        for i in prerequisites:
            dct[i[1]].append(i[0])
        # BFS
        for key, item in dct.items():
            seen = {}
            while item:
                current = item.pop(0)
                seen[current] = True
                if current == key:  # lop is detected
                    return False
                if current in dct:
                    for element in dct[current]:
                        if element in seen:
                            continue
                        item.append(element)
        return True
