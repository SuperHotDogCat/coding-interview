"""
Reference
shining-aiさん: https://github.com/shining-ai/leetcode/pull/34/files
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/44#discussion_r1551313218
マジックナンバーだとわかりにくいという意見を反映, mとnよりもheightとwidthと名前にする。
これも空間計算量を減らせる気がしたのでやってみたが, phase1のように考えるとcolumnの方向に岩がある時のテストケースで弾かれるので, ちょっと工夫がやはり必要
hayashi-ayさんのphase4を参考に組んだ
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        OBSTACLE = 1
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        num_unique_path = [0 for _ in range(width)]
        for row in range(height):
            for col in range(width):
                if obstacleGrid[row][col] == OBSTACLE:
                    num_unique_path[col] = 0
                elif row == 0 and col == 0:
                    num_unique_path[0] = 1
                elif col > 0:
                    num_unique_path[col] += num_unique_path[col-1]
        return num_unique_path[width-1]