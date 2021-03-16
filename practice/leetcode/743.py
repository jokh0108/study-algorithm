#  https://leetcode.com/problems/network-delay-time/
from typing import List

import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        def dijkstra(start: int) -> dict:
            dist = collections.defaultdict(int)
            q = [(0, k)]
            while q:
                time, node = heapq.heappop(q)
                if node not in dist:
                    dist[node] = time
                    for v, w in graph[node]:
                        alt = time + w
                        heapq.heappush(q, (alt, v))

            return dist

        costs = dijkstra(k)
        if len(costs) != n:
            return -1
        return max(costs.values())


solution = Solution()
print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
