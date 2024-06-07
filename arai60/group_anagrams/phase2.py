"""
Reference
sakupan102さん: https://github.com/sakupan102/arai60-practice/pull/13/files
YukiMichishitaさん: https://github.com/YukiMichishita/LeetCode/pull/5/files
sorted_string_to_anagramsという命名はphase1でつけるかを悩み, 大袈裟だと思いstring_to_anagramにしたが, そうした方がわかりやすかったらしいので変更した
dictのvalueをまとめるのにlist(sorted_str_to_anagrams.values())という方法があったかと思い, 採用する

hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/19/files ランレングスで符号化する方法もありではあるのかと言う気持ちに
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_string_to_anagrams = defaultdict(list) 
        for string in strs:
            sorted_string = "".join(sorted(string)) 
            sorted_string_to_anagrams[sorted_string].append(string)
        
        return list(sorted_string_to_anagrams.values())