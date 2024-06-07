def create_string_index_to_column_index(numRows: int)->dict:
    string_index_to_column_index = {}
    for string_index in range(numRows):
        column_index = string_index 
        string_index_to_column_index[string_index] = column_index
    for difference_index in range(numRows-2):
        string_index = numRows + difference_index
        column_index = numRows - difference_index - 2
        string_index_to_column_index[string_index] = column_index
    # return dict: {0:0, 1:1, ..., numRows-1: numRows-1, numRows: numRows-2, ..., 2*numRows-3:1}
    return string_index_to_column_index

def create_remain_string_index(string_index, numRows):
    if numRows == 1:
        return 0
    return string_index % (2 * numRows - 2)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        concat_strings = ["" for _ in range(numRows)] #Store the strings of each column
        string_index_to_column_index = create_string_index_to_column_index(numRows) #dict: string_index->column_index
        for string_index, string in enumerate(s):
            column_index = string_index_to_column_index[create_remain_string_index(string_index, numRows)]
            concat_strings[column_index] += string
        concated_string = ""
        for string in concat_strings:
            concated_string += string
        return concated_string