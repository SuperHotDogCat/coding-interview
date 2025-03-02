# 単純にBFSをしてtime limit overしたもの, そりゃそうだろうなという感じの時間計算量
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        for word in wordList:
            if word == endWord: # ここ, if endWord not in wordListで効率化できるな
                break
        else:
            return 0 # もしwordListになければreturnする

        def calc_word_diff(s1: str, s2: str) -> int:
            word_diff_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    word_diff_count += 1
            return word_diff_count
        queue = deque([(beginWord, wordList, 1)])
        while queue:
            tail_word, available_words, sequence_length = queue.popleft()
            if tail_word == endWord:
                return sequence_length
            for word in available_words:
                if calc_word_diff(tail_word, word) == 1:
                    next_available_words = available_words.copy()
                    next_available_words.remove(word)
                    queue.append((word, next_available_words, sequence_length + 1))

        return 0

# 前もってグラフを作っておいてBFS, seenで管理しているので最大でもO(5000^2)なはず。通りはしたがなんか遅い, 何か間違えている気がする
# seenで管理するのは今回はshortest pathなのでBFSで最初についたルートでseenに追加したとしても問題ないからだと考えている
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        for word in wordList:
            if word == endWord: # ここ, if endWord not in wordListで効率化できるな
                break
        else:
            return 0 # もしwordListになければreturnする

        def calc_word_diff(s1: str, s2: str) -> int:
            word_diff_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    word_diff_count += 1
            return word_diff_count
        
        word_graph = defaultdict(list)
        for word in wordList:
            if calc_word_diff(beginWord, word) == 1:
                word_graph[beginWord].append(word)
        
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if calc_word_diff(wordList[i], wordList[j]) == 1:
                    word_graph[wordList[i]].append(wordList[j])
                    word_graph[wordList[j]].append(wordList[i])
        
        seen = set()
        queue = deque([(beginWord, 1)])
        while queue:
            tail_word, sequence_length = queue.popleft()
            for next_word in word_graph[tail_word]:
                if next_word == endWord:
                    return sequence_length + 1
                if next_word in seen:
                    continue
                seen.add(next_word)
                queue.append((next_word, sequence_length + 1))

        return 0
