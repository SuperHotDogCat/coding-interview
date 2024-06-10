class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            self.uniquePaths(n, m)
        num_unique_path = [1 for _ in range(m)]
        for row in range(1, n):
            for col in range(1, m):
                num_unique_path[col] += num_unique_path[col-1]
        return num_unique_path[m-1]