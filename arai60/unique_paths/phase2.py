"""
Reference
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/39/files
shining-aiさん: https://github.com/shining-ai/leetcode/pull/32/files
一応i, jではなくcol, rowなりwidth, heightなりの名前にした方がいいかなと思った。
空間計算量O(min(m,n))の解答も書いてみることに
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_unique_path = [[0 for _ in range(n)] for _ in range(m)]
        # num_unique_paths[i][j] means the number of unique paths from (0, 0) to (i, j)
        # init unique_paths
        for row in range(m):
            num_unique_path[row][0] = 1
        for col in range(n):
            num_unique_path[0][col] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                num_unique_path[row][col] = num_unique_path[row-1][col] + num_unique_path[row][col-1]
        return num_unique_path[m-1][n-1]
    
# O(min(m,n))の解答 結構解読に時間がかかった。
# shining-aiさんのnum_unique_path = [1] * mはあるcolでのrowの値を保存している。
# num_unique_path[row] += num_unique_path[row - 1]はnum_unique_path[row - 1]があるcolでのnum_unique_path[row - 1]の値を足しており, 
# 代入される前のnum_unique_path[row]はあるcolの一つ前の値を保存しているのでphase1の回答と等価になる

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            self.uniquePaths(n, m)
        num_unique_path = [1 for _ in range(m)]
        for row in range(1,n):
            for col in range(1,m):
                num_unique_path[col] +=  num_unique_path[col-1]
        return num_unique_path[m-1]