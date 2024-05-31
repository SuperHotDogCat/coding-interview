class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = [False] * len(s)
        is_tokenizable = [False] * len(s)
        def check_tokenizable(start):
            if start >= len(s):
                return 
            if seen[start]:
                return 
            seen[start] = True
            for word in wordDict:
                if s.startswith(word, start):
                    is_tokenizable[start+len(word)-1] = True
                    check_tokenizable(start+len(word))
            return 
        check_tokenizable(0)
        return is_tokenizable[-1]