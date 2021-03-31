from typing import List

import heapq


class Solution:
    def canCompleteCircuit(self, gases: List[int], costs: List[int]) -> int:
        answer = -1
        for start in range(len(gases)):
            if gases[start] - costs[start] < 0:
                continue
            prev = start
            next = (start + 1) % len(gases)
            remain = gases[start]
            while next != start:
                prev = next
                next = (next + 1) % len(gases)
                remain = remain - costs[prev] + gases[next]


solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
