"""
743. Network Delay Time
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.


Dijkstra   Greedy
each time from the starting chose the smallest value available
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        # create adjancy list
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]  # initial wieght zero, k starting node
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue  # dont need to revisit
            visit.add(n1)  # adding to set if not visited
            t = max(t, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))  # weight is considered since starting node

        return t if n == len(visit) else -1


class Slow_solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [float("inf")] * (n + 1)
        graph[0] = float("-inf")
        graph[k], q = 0, [k]
        dct = defaultdict(list)
        for item in times:
            dct[item[0]].append(item[1:])
        while q:
            current = float("inf")
            for element in q:
                current = element if graph[element] < current else current
            q.remove(current)
            for item in dct[current]:
                if item[1] + graph[current] < graph[item[0]]:
                    graph[item[0]] = item[1] + graph[current]
                    q.append(item[0])
        return -1 if float("inf") in graph else max(graph)


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times=[[1, 2, 1], [2, 1, 3]], n=2, k=1))
