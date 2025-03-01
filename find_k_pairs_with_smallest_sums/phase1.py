# 最初はmerge sortのmergeのように解こうとしたがその方法だと自分の実装ミスなのかわからないがnums1のindexが前に戻らないとsmallest sumsを見つけられないパターンがあったのでやめる
# 最初nums1を固定してheapにいれて答えの候補になりえるnums1をどんどん増やしていくことにした
# 空間計算量O(k), 時間計算量: O(klogk)

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k_smallest_pairs = []
        min_heap = []
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j)) # nums1[0]とのpairを作る
        
        while len(k_smallest_pairs) < k:
            _, i, j = heapq.heappop(min_heap)
            k_smallest_pairs.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j)) # nums1[i + 1]とnums2[j]のpairが次のk smallestとなりうる
        
        return k_smallest_pairs
