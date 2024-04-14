class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        longest_length_substring = 0
        recently_seen = {} # Store the index of the most recently seen string
        for right_pointer in range(len(s)):
            current_focus_char = s[right_pointer]
            if current_focus_char in recently_seen and recently_seen[current_focus_char] >= left_pointer:
                # current_focus_char in recently_seen: already seen
                # recently_seen[current_focus_char] >= left_pointer: current_focus_char is between left_pointer and right_pointer
                left_pointer = recently_seen[current_focus_char] + 1 # shift left_pointer
            else:
                longest_length_substring = max(longest_length_substring, right_pointer - left_pointer + 1) # retrieve the bigger length
            
            recently_seen[current_focus_char] = right_pointer

        return longest_length_substring