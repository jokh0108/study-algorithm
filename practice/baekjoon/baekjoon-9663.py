# N-Queen
import sys

N = int(sys.stdin.readline())


class Solution:
    def __init__(self, N):
        self.N = N
        self.count = 0

    def promising(self, row, col, queens):
        for i in range(1, row + 1):
            if (
                ((row - i, col) in queens)
                or ((row - i, col - i) in queens)
                or ((row - i, col + i) in queens)
            ):
                return False
        return True

    def n_queen(self, row, queens):
        if row == N:
            self.count += 1
            return
        for col in range(N):
            if self.promising(row, col, queens):
                self.n_queen(row + 1, queens | set([(row, col)]))

    def main(self, N):
        for col in range(N):
            self.n_queen(1, set([(0, col)]))
        return self.count


solution = Solution(N)
print(solution.main(N))
