class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            self.uniquePaths(n, m)
        num_unique_path = [1 for _ in range(m)]
        for col in range(1, n):
            for row in range(1, m):
                num_unique_path[row] += num_unique_path[row-1]
        return num_unique_path[m-1]