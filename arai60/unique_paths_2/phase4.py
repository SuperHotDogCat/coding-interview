class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_unique_path = [0 for _ in range(width)]
        num_unique_path[0] = 1
        for row in range(height):
            for col in range(width):
                if obstacleGrid[row][col] == OBSTACLE:
                    num_unique_path[col] = 0
                elif col > 0:
                    num_unique_path[col] += num_unique_path[col-1]
        return num_unique_path[width-1]