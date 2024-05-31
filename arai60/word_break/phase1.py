# 配列を使ったdp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        is_word_break = [False for _ in range(len(s))] 
        # is_word_break means s[:i+1] can be broken.
        for i, c in enumerate(s):
            string_from_beginning = s[:i+1]
            for word in wordDict:
                if string_from_beginning == word:
                    is_word_break[i] = True
                elif i+1-len(word) >= 0 and s[i+1-len(word):i+1] == word and is_word_break[i-len(word)]:
                    is_word_break[i] = True
        return is_word_break[len(s)-1]

# 再起的なdp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        is_word_break = [False for _ in range(len(s))]
        seen = [False for _ in range(len(s))]
        def recursiveWordBreak(index, seen, is_word_break):
            if index >= len(s):
                return 
            if seen[index]:
                return 
            string_from_beginning = s[:index+1]
            for word in wordDict:
                if string_from_beginning == word:
                    seen[index] = True
                    is_word_break[index] = True
                    return recursiveWordBreak(index+1, seen, is_word_break)
                elif index+1-len(word) >= 0 and word == s[index+1-len(word):index+1] and is_word_break[index-len(word)]:
                    seen[index] = True
                    is_word_break[index] = True
                    return recursiveWordBreak(index+1, seen, is_word_break)
            seen[index] = True
            return recursiveWordBreak(index+1, seen, is_word_break)
        recursiveWordBreak(0, seen, is_word_break)
        return is_word_break[len(s)-1]

# タイムアウトしたコード, 本質的にはメモしてない再帰のように考える探索木が爆発してしまったと考えられる。
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        char_to_string = defaultdict(list)
        for string in wordDict:
            char_to_string[string[0]].append(string)
        stack = [0]
        while stack:
            cursor = stack.pop()
            if cursor >= len(s):
                return True
            
            beginning_char = s[cursor]
            for string in char_to_string[beginning_char]:
                if s[cursor:cursor+len(string)] in char_to_string[beginning_char]:
                    stack.append(cursor+len(string))
        return False
