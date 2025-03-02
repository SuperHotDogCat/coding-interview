# @hardjuice @tohsumi @colorbox @pompom0x0 @takkatao 
# https://github.com/olsen-blue/Arai60/pull/20/files 
# - 遷移のさせ方、には一工夫必要。ある単語(例：hot)から、変化のさせ方としては、３パターン存在する。
#    - 具体的には、「*ot」「h*t」「ho*」の3パターンである。これらをキーとして、対応する単語を、辞書管理すれば良さそう。
#    - 「hot」 ->「*ot」「h*t」「ho*」という変換が、必要そう。
# このまとめ方が参考になった, 文字列の結合でなくてtupleをkeyにするというのも確かにと思った
# get_keys_from_word(word)で結局O(n)かかるので自分と同じような実行時間になるのかしら...?
# https://github.com/colorbox/leetcode/pull/34/files
# https://github.com/Hurukawa2121/leetcode/pull/20#pullrequestreview-2569671996
# https://github.com/t0hsumi/leetcode/pull/20
# https://github.com/tshimosake/arai60/pull/11#discussion_r1944112516
# ordを一応確認 https://github.com/t0hsumi/leetcode/pull/12#discussion_r1886759238

# 最初にグラフを作らなくてもよかった
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
        
        seen = set()
        queue = deque([(beginWord, 1)])
        while queue:
            tail_word, sequence_length = queue.popleft()
            for word in wordList:
                if word not in seen and calc_word_diff(tail_word, word) == 1:
                    if word == endWord:
                        return sequence_length + 1
                    queue.append((word, sequence_length + 1))
                    seen.add(word)
        return 0
# 書いてから思ったけど1に等しいかどうかで判断する方が綺麗かも
# def is_connectable(s1: str, s2: str) -> bool:
#     count = 0
#     for i in range(len(s1)):
#         if s1[i] != s2[i]:
#             count += 1
#     return count == 1

# 1文字違う←→1文字だけ入れ替えたものがhitするかで判断, ただまあ早くはなったんですが文字の読みにくくなった気がする。calc_word_diffみたいに関数名にした方が好きかも
# あとはこのコードだと英語小文字以外で対応ができない, 拡張がだるい, 文字コード全部対象だとlower_characters = 'abcdefghijklmnopqrstuvwxyz'のところが長くてつらいなあという感じでしょうか
# このコードがボトルネックで, サービスに影響を与えるなら使うか程度?
class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([[beginWord, 1]])
        lower_characters = 'abcdefghijklmnopqrstuvwxyz'
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in lower_characters:
                    next_word = word[:i] + c + word[i + 1:] # chr(ord('a') + [0:26]の数)でも良い
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

# key_to_words, word_to_keysを作ってwhile文内部の処理を早くする放法
# key = (beginWord[:i], beginWord[i + 1:])という処理, 早くはなるんだけどやはりコメントを付与してあげないと一見してわからないコードかも?
class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        key_to_words = defaultdict(list)
        word_to_keys = defaultdict(list)
        for i in range(len(beginWord)):
            key = (beginWord[:i], beginWord[i + 1:]) # 1文字違うことを示す ex. hot -> *ot, h*t, ho*のようにおこなう
            key_to_words[key].append(beginWord)
            word_to_keys[beginWord].append(key)

        for word in wordList:
            for i in range(len(word)):
                key = (word[:i], word[i + 1:])
                key_to_words[key].append(word)
                word_to_keys[word].append(key)
        
        if endWord not in word_to_keys:
            return 0

        seen = set([beginWord])
        queue = deque([(beginWord, 1)])
        while queue:
            tail_word, sequence_length = queue.popleft()
            for key in word_to_keys[tail_word]:
                for word in key_to_words[key]:
                    if word not in seen:
                        if word == endWord:
                            return sequence_length + 1
                        queue.append((word, sequence_length + 1))
                        seen.add(word)
        return 0
