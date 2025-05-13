"""
56. Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

from typing import List
# Time O (N*LOGN)
# Space: O(N) or O(log N) if the intervals are merged and we do not need to store all
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res, srt= [],sorted(intervals,key=lambda x:(x[0], x[1]))
        for el in srt:
            if not res or res[-1][1] < el[0]:
                res. append(el)
            else:
                res[-1][1]=max(el[1],res[-1][1])
        return res




# Without Sort it will be O(N^2)
#  Using the default dict and raph to store all intervals within similar tuple enteries

import collections
class No_SORT_Solution:
    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def buildGraph(self, intervals):
        graph = collections.defaultdict(list)

        for i, interval_i in enumerate(intervals):
            for j in range(i+1, len(intervals)):
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def getComponents(self, graph, intervals):
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1

        return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.buildGraph(intervals)
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]
