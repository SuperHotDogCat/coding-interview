class Solution:
    def isValid(self, s: str) -> bool:
        close_brackets_to_open_brackets = {")":"(", "}": "{", "]": "["}
        open_brackets = close_brackets_to_open_brackets.values()
        seen_open_brackets = [] #既にみたopen bracket
        for char in s:
            if char in open_brackets:
                # 追加
                seen_open_brackets.append(char)
            
            elif char in close_brackets_to_open_brackets:
                if len(seen_open_brackets) == 0:
                    # seen_open_bracketsが空の場合, 対応するopen_bracketはない
                    return False
                
                elif close_brackets_to_open_brackets[char] != seen_open_brackets.pop():
                    return False
        # もし空じゃないなら未処理のopen_bracketが残っている
        return not seen_open_brackets