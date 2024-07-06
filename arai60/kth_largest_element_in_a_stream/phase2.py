"""
Reference:
ryoooooory: https://github.com/ryoooooory/LeetCode/pull/15/files
seal-azarashi: https://github.com/seal-azarashi/leetcode/pull/8#pullrequestreview-2153924472
Yoshiki-Iwasa: https://github.com/Yoshiki-Iwasa/Arai60/pull/7
kazukiii: https://github.com/kazukiii/leetcode/pull/9/files
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/54/files
cheeseNA: https://github.com/cheeseNA/leetcode/pull/12/files

add method以外でmin_heap propertyをいじって欲しくないのでアンダーバーをつけてprivateであることを主張して書くべきだと感じた
ryooooooryさんのコメントにあった: 順次追加処理かつソート操作に強いPriorityQueueで実装とあったので少し頭の片隅にいれておく

"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._min_heap = [] # _min_heap has k elements and _min_heap[0] means the k-th largest element in the stream
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self._min_heap) < self.k:
            heapq.heappush(self._min_heap, val)
        elif val > self._min_heap[0]:
            heapq.heappushpop(self._min_heap, val)
        
        return self._min_heap[0]

# 別のheapq実装もためす。https://docs.python.org/ja/3/library/heapq.htmlにはheappushpopを使った方が1回ずつpushとpopを呼び出すよりも効率が良いので, 上の方が良い?
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._min_heap = [] # _min_heap has k elements and _min_heap[0] means the k-th largest element in the stream
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add new value and pop until len(self._min_heap) == self.k
        heapq.heappush(self._min_heap, val)
        while len(self._min_heap) > self.k:
            heapq.heappop(self._min_heap)
        
        return self._min_heap[0]
