# ascii_histogram = [0 for _ in range(256)]
# string_histograms = [[] for _ in range(len(strs))]
# とし, ord(char)の値を加算していって, 
# 最後にできたhistorgramをjoinして0と1の文字列にしてkeyにした辞書に要素を加えて行こうとしたが....
# "bdddddddddd","bbbbbbbbbbc"というテストケースでこの方法だとkeyが衝突した。

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_to_anagrams = defaultdict(list) # key: sorted string, value: raw string
        for string in strs:
            sorted_string = "".join(sorted(string)) 
            string_to_anagrams[sorted_string].append(string)
        
        group_anagrams: List[List[int]] = []
        for anagrams in string_to_anagrams.values():
            group_anagrams.append(anagrams)
        
        return group_anagrams