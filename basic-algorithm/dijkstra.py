#  https://leetcode.com/problems/network-delay-time/
from typing import List

import collections
import heapq


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    def dijkstra(start: int) -> dict:
        dist_dic = collections.defaultdict(int)
        pq = [(0, start)]
        while pq:
            time, node = heapq.heappop(pq)
            if node not in dist_dic:
                dist_dic[node] = time
                for v, w in graph[node]:
                    heapq.heappush(pq, (time + w, v))
        return dist_dic

    costs = dijkstra(k)
    if len(costs) != n:
        return -1
    return max(costs.values())


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
