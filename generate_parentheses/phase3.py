class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        valid_parentheses = [] # 有効な答えを格納するコンテナ
        under_processing_parentheses = [("", n, n)] # stack
        while under_processing_parentheses:
            current_parentheses, remain_open_bracket_count, remain_close_bracket_count = under_processing_parentheses.pop()

            if remain_open_bracket_count == 0 and remain_close_bracket_count == 0:
                valid_parentheses.append(current_parentheses)
                continue
            
            if 0 < remain_open_bracket_count:
                # 使える(があるときはいつ加えてもvalidなparenthesesになる
                under_processing_parentheses.append((current_parentheses + "(", remain_open_bracket_count - 1, remain_close_bracket_count))
            
            if remain_open_bracket_count < remain_close_bracket_count:
                #　remain_open_bracket_count < remain_close_bracket_count の時だけvalidなparenthesesが作れる
                under_processing_parentheses.append((current_parentheses + ")",remain_open_bracket_count, remain_close_bracket_count - 1))

        return valid_parentheses