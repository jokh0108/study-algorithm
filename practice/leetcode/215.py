from typing import List

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[k-1]

        # maxheap = [-x for x in nums]
        # heapq.heapify(maxheap)
        # for _ in range(k-1):
        #     heapq.heappop(maxheap)
        # return -heapq.heappop(maxheap)


solution = Solution()
print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))
