class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_paths = [[0 for _ in range(n)] for _ in range(m)]
        # num_unique_paths[i][j] means the number of unique paths from (0, 0) to (i, j)
        # init unique_paths
        for i in range(m):
            num_unique_paths[i][0] = 1
        for j in range(n):
            num_unique_paths[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                num_unique_paths[i][j] = num_unique_paths[i-1][j] + num_unique_paths[i][j-1]
        return num_unique_paths[m-1][n-1]

"""
以下はおふざけ

def factorial(n: int)->List[int]:
    factorials = [0 for _ in range(n+1)]
    factorials[0] = 1
    for i in range(1, n+1):
        factorials[i] = factorials[i-1] * i
    return factorials

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        needed_factorials = factorial(m+n-2) # factorials from 0 to m+n-2
        return factorials[m+n-2] // factorials[m-1] // factorials[n-1] # combinations theory
"""