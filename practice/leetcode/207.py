from typing import List

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        traced = set()
        visited = set()
        graph = collections.defaultdict(list)

        def dfs(v):
            if v in traced:
                return False
            if v in visited:
                return True

            traced.add(v)
            for w in graph[v]:
                if not dfs(w):
                    return False
            traced.remove(v)
            visited.add(v)
            return True

        for a, b in prerequisites:
            graph[a].append(b)

        for x in list(graph):
            if not dfs(x):
                return False

        return True


solution = Solution()
print(solution.canFinish(2, [[0, 1]]))
print(solution.canFinish(2, [[1, 0]]))
print(solution.canFinish(2, [[1, 0], [0, 1]]))
