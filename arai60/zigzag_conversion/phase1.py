def create_string_index_to_store_index(numRows: int)->dict:
    string_index_to_store_index = {}
    for index in range(numRows):
        string_index_to_store_index[index] = index
        #{0: 0, 1: 1, 2: 2, ..., numRows - 1: numRows - 1}
    for index in range(numRows-2):
        string_index_to_store_index[index + numRows] = numRows - index - 2
    # 周期2*numRows - 2で変化するindexの辞書ができた
    return string_index_to_store_index

def string_index(index, numRows):
    if numRows == 1:
        return 0
    return index % (2 * numRows - 2)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        concat_strings = ["" for _ in range(numRows)]
        string_index_to_store_index = create_string_index_to_store_index(numRows)
        for index, string in enumerate(s):
            concat_strings[string_index_to_store_index[string_index(index, numRows)]] += string
        concated_string = ""
        for string in concat_strings:
            concated_string += string
        return concated_string