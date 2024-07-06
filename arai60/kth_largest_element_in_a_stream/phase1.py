# 普通に苦戦した
# 思考録: Quick selectアルゴリズムを思いつく, だが動的に配列が変化するので無駄に計算が増え, 他に効率が良いものがないか考える
# じゃあdequeでmax_len=kを指定してやれば良いかなと思ったが, これだと結局途中に要素を挿入するときに時間計算量がO(k)程度かかるので断念
# 要素数をkに保ったmin_heapのrootを出力する方向で制作, これなら挿入操作もO(logk)程度で良い
# heapqを覚えていなかったのでhttps://docs.python.org/ja/3/library/heapq.htmlを確認した。
# heapq.heapreplaceかheapq.heappushpopのどちらを使うか迷う。前者はpopしてからpush, 後者はpushしてからpopでどちらも要素数は保存されるのでどちらでも良いかなと思ったが...
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = [] # min_heap has k elements and min_heap[0] means the k-th largest element in the stream
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        
        return self.min_heap[0]
