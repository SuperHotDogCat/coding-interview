class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def is_connectable(s1: str, s2: str) -> bool:
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count == 1
        
        seen = set([beginWord])
        queue = deque([(beginWord, 1)])
        while queue:
            tail_word, sequence_length = queue.popleft()
            for word in wordList:
                if word not in seen and is_connectable(word, tail_word):
                    if word == endWord:
                        return sequence_length + 1
                    queue.append((word, sequence_length + 1))
                    seen.add(word)
        return 0
