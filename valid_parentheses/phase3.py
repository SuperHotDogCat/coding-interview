class Solution:
    def isValid(self, s: str) -> bool:
        close_brankets_to_open_brankets = {")":"(", "}": "{", "]": "["}
        open_brankets = close_brankets_to_open_brankets.values()
        seen_open_brankets = [] #既にみたopen branket
        for char in s:
            if char in open_brankets:
                # 追加
                seen_open_brankets.append(char)
            
            elif char in close_brankets_to_open_brankets:
                if len(seen_open_brankets) == 0:
                    # seen_open_branketsが空の場合, 対応するopen_branketはない
                    return False
                
                elif close_brankets_to_open_brankets[char] != seen_open_brankets.pop():
                    return False
        # もし空じゃないなら未処理のopen_branketが残っている
        return not seen_open_brankets