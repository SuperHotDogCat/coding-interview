class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = [False for _ in range(len(s))]
        is_tokanizable = [False for _ in range(len(s))]
        def check_tokanizable(start, seen, is_tokanizable):
            if start >= len(s):
                return 
            if seen[start]:
                return 
            seen[start] = True
            for word in wordDict:
                if s.startswith(word, start):
                    is_tokanizable[start+len(word)-1] = True
                    check_tokanizable(start+len(word), seen, is_tokanizable)
            return 
        check_tokanizable(0, seen, is_tokanizable)
        return is_tokanizable[-1]