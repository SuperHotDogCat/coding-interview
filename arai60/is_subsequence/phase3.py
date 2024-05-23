class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_index = 0
        for c in t:
            if c == s[s_index]:
                s_index += 1
            if s_index >= len(s):
                return True
        return False