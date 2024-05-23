class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        cursor_of_s = 0
        for char_of_t in t:
            if char_of_t == s[cursor_of_s]:
                cursor_of_s += 1
            if cursor_of_s >= len(s):
                return True
        return False