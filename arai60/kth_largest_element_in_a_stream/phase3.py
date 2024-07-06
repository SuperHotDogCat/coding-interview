class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._min_heap = [] # _min_heap has k elements and _min_heap[0] means the k-th largest element in the stream.
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self._min_heap) < self.k:
            heappush(self._min_heap, val)
        elif val >= self._min_heap[0]:
            heappushpop(self._min_heap, val)

        return self._min_heap[0]