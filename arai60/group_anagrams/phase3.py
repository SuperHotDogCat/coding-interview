# 時間計算量 O(strs.length * strs[i].length * log(strs[i].length))
# 空間計算量 O(strs.length)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_string_to_anagrams = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string))
            sorted_string_to_anagrams[sorted_string].append(string)
        return list(sorted_string_to_anagrams.values())