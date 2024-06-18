class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 状態を格納する変数を少なくするアプローチ
        valid_parentheses = [] # 有効な答えを格納するコンテナ
        under_processing_parentheses = [""] # stack
        while under_processing_parentheses:
            current_parentheses = under_processing_parentheses.pop()

            if current_parentheses.count("(") == n and current_parentheses.count(")") == n:
                valid_parentheses.append(current_parentheses)
                continue
            
            if current_parentheses.count("(") < n:
                # 使える(があるときはいつ加えてもvalidなparenthesesになる
                under_processing_parentheses.append(current_parentheses + "(")
            
            if current_parentheses.count(")") < current_parentheses.count("("):
                under_processing_parentheses.append(current_parentheses + ")")

        return valid_parentheses

# 再帰で書く場合

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _generate_valid_parentheses(current_parenthesis: str, n: int)->List[str]:
            if current_parenthesis.count("(") == n and current_parenthesis.count(")") == n:
                return [current_parenthesis]
            
            valid_parentheses = []
            if current_parenthesis.count("(") < n:
                valid_parentheses += _generate_valid_parentheses(current_parenthesis + "(", n)
            if current_parenthesis.count(")") < current_parenthesis.count("("):
                valid_parentheses += _generate_valid_parentheses(current_parenthesis + ")", n)
            
            return valid_parentheses
        
        return _generate_valid_parentheses("", n)