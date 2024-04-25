class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_to_index = {}
        max_length = 0
        for right, c in enumerate(s):
            if c in char_to_index and char_to_index[c] >= left:
                left = char_to_index[c] + 1
            
            max_length = max(max_length, right - left + 1)
            char_to_index[c] = right
        
        return max_length