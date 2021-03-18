from typing import List


class Solution:

    @staticmethod
    def getDistance(p):
        return (p[0]**2 + p[1]**2)**0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=self.getDistance)[:k]


solution = Solution()
print(solution.kClosest([[1, 3], [-2, 2]], 1))
print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
