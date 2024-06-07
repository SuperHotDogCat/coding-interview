"""
Reference
shining-ai san: https://github.com/shining-ai/leetcode/pull/60/files
周期を考えて, 何番目のrowにいれるかという解法をstep1-3から書いてきたが, 
shining-aiのコードを見てrowの移動方向を変える方が頭のリソースの節約にも, 
空間計算量の節約にもつながることに気づいたので使ってみます


"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row_strings = [[] for _ in range(numRows)]
        
        direction = 1
        row_index = 0
        for c in s:
            row_strings[row_index].append(c)

            if row_index == 0:
                direction = 1
            elif row_index == numRows - 1:
                direction = -1
            
            row_index += direction
        
        return "".join(row_char for row_string in row_strings for row_char in row_string)