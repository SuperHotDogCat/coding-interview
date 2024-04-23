class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_parentheses = []
        under_processing_parentheses = ["("]
        while under_processing_parentheses:
            current_parenthesis = under_processing_parentheses.pop()
            open_bracket_count = current_parenthesis.count("(")
            closed_bracket_count = current_parenthesis.count(")")

            add_parentheses = []
            if closed_bracket_count == open_bracket_count:
                # closed_bracket_count == open_bracket_countな状態でclosed_bracketを追加するとinvalidな状態になる
                add_parentheses.append(current_parenthesis + "(")
            elif open_bracket_count == n:
                # open_bracketを使い切ったら文字列の長さが2*nになるまでclosed_bracketを追加
                add_parentheses.append(current_parenthesis + ")")
            else:
                # それ以外はどのbracketを使い切ってもvalidな状態になりえる途中経過状態になる
                add_parentheses.append(current_parenthesis + "(")
                add_parentheses.append(current_parenthesis + ")")
            
            for add_parenthesis in add_parentheses:
                if len(add_parenthesis) == 2*n:
                    # terminate
                    valid_parentheses.append(add_parenthesis)
                
                else:
                    # 追加
                    under_processing_parentheses.append(add_parenthesis)

        return valid_parentheses