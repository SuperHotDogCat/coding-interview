# discordで他の人の回答も見てみた。
# 結構な人が文字列をガチャガチャしていていた
# https://github.com/nittoco/leetcode/pull/4/files, https://github.com/hayashi-ay/leetcode/pull/71/files
# 僕も最初思いついた解法は, 1行目は周期ずつ文字列を飛ばす, 2行目は周期ずつ文字列を飛ばし, 
# 何個か戻ったところに文字があるのでそれを回収してくる...のような方法でいこうとしたが, 頭がこんがらがってしまい, 他にいい方法がないかを考えてみた。
# i行目にある文字は表現するためには, 文字列のj-index番目とnumRowsに関する何らかの余りで表現できることに気づいたので, それを用いた。

def create_string_index_to_col_index(numRows: int)->dict:
    string_index_to_col_index = {}
    for string_index in range(numRows):
        col_index = string_index
        string_index_to_col_index[string_index] = col_index
        #{0: 0, 1: 1, 2: 2, ..., numRows - 1: numRows - 1}
    for difference_index in range(numRows - 2):
        string_index = numRows + difference_index
        col_index = numRows - difference_index - 2
        string_index_to_col_index[string_index] = col_index
    # 周期2*numRows - 2で変化するindexの辞書ができた
    #{0: 0, 1: 1, 2: 2, ..., numRows - 1: numRows - 1, numRows: numRows - 2, ..., 2 * numRows - 3: 1}
    return string_index_to_col_index

def create_col_index(index, numRows):
    if numRows == 1:
        return 0
    return index % (2 * numRows - 2)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        concat_strings = ["" for _ in range(numRows)]
        string_index_to_col_index = create_string_index_to_col_index(numRows)
        for string_index, string in enumerate(s):
            concat_strings[string_index_to_col_index[create_col_index(string_index, numRows)]] += string
        concated_string = ""
        for string in concat_strings:
            concated_string += string
        return concated_string

print(create_string_index_to_col_index(3))