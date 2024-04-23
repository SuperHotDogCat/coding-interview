class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_parentheses = []
        under_processing_parentheses = [("", n, n)] #initial state

        while under_processing_parentheses:
            current_parentheses, remain_open_bracket_count, remain_close_bracket_count = under_processing_parentheses.pop()
            if remain_open_bracket_count == 0 and remain_close_bracket_count == 0:
                valid_parentheses.append(current_parentheses)
                continue

            if 0 < remain_open_bracket_count:
                under_processing_parentheses.append((current_parentheses + "(", remain_open_bracket_count - 1, remain_close_bracket_count))
            if remain_open_bracket_count < remain_close_bracket_count:
                under_processing_parentheses.append((current_parentheses + ")", remain_open_bracket_count, remain_close_bracket_count - 1))
            
        return valid_parentheses
    
"""
phase1と同じようにvalidな状態から終了状態までの遷移グラフを追うようなコードにした

Reference:
https://github.com/ryoooooory/LeetCode/pull/6/files
refactoredSolution2.javaが近いのかなと感じた。

https://github.com/shining-ai/leetcode/pull/53/files
再帰で解く解き方も確かにできますね。level4のコードが綺麗ですし, 僕のphase1のコードで感じていた
add_parenthesisとadd_parenthesesを複数形と単数系で区別するのはなんだか認知負荷がかかるなあという思いがあったのでとても参考になりました。

"""