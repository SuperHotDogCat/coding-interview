# https://github.com/Fuminiton/LeetCode/pull/10/files heappopがlen(container) == 0の時のエラー挙動は確かに頭から外れていた, 今回はこういうことはないのだけれど, ちょっと意識 visited変数で行ったところを管理する方が書く側としては確かに楽だなあと思った
# https://github.com/fuga-98/arai60/pull/11/files ここでも同じコメントが, heappopがlen(container) == 0の時にエラーが起きないかとかは気にした方がいいと思いつつも, どうしよう, 最初の1行目にassert k <= len(nums1) * len(nums2)であることを確認しておこうかなと
# https://github.com/BumbuShoji/Leetcode/pull/11/filesなので1 <= nums1.length, nums2.length <= 10^5だとMemory Limitが起きるという指摘が,確かに
# https://github.com/olsen-blue/Arai60/pull/10/files 

# visited変数を使って書く

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        assert k <= len(nums1) * len(nums2) # k pairsが必ずできることを保証する
        k_smallest_pairs = []
        min_heap = []
        seen = set() # seen pairs
        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        
        while len(k_smallest_pairs) < k:
            _, i, j = heapq.heappop(min_heap)
            k_smallest_pairs.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i + 1, j) not in seen:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                seen.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in seen:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                seen.add((i, j + 1))
        
        return k_smallest_pairs

# こっちの方が好みかも
