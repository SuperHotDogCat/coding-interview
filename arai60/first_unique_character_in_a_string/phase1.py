class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 登場回数を数える
        count_appearance = [0 for _ in range(128)]
        for char in s:
            count_appearance[ord(char)] += 1

        for index, char in enumerate(s):
            if count_appearance[ord(char)] == 1:
                return index
        return -1
