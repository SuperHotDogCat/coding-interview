class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_appear_count = defaultdict(int)
        for c in s:
            char_to_appear_count[c] += 1
            
        for index, c in enumerate(s):
            if char_to_appear_count[c] == 1:
                return index
        return -1