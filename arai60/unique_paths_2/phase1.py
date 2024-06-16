class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        num_unique_paths = [[0 for _ in range(n)] for _ in range(m)]
        # num_unique_paths[i][j] means the number of unique paths from (0, 0) to (i, j)
        # init unique_paths
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            num_unique_paths[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            num_unique_paths[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                num_unique_paths[i][j] = num_unique_paths[i-1][j] + num_unique_paths[i][j-1]
        return num_unique_paths[m-1][n-1]