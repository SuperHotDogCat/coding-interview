class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        recently_seen = dict()
        left_pointer = 0
        longest_length_substring = 0
        for right_pointer in range(len(s)):
            current_focus_string = s[right_pointer]
            if current_focus_string in recently_seen and recently_seen[current_focus_string] >= left_pointer:
                # current_focus_string in recently_seen: みたことがある
                # recently_seen[current_focus_string] >= left_pointer 現在注目している区間内にcurrent_focus_stringが含まれている
                left_pointer = recently_seen[current_focus_string] + 1
            else:
                longest_length_substring = max(longest_length_substring, right_pointer - left_pointer + 1)
            
            # 最後に見た位置を更新
            recently_seen[current_focus_string] = right_pointer
        return longest_length_substring