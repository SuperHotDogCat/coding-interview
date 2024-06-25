"""
Reference
ryotaro: https://github.com/Ryotaro25/leetcode_first60/pull/14/files
mike: https://github.com/Mike0121/LeetCode/pull/30/files
kazukiii: https://github.com/kazukiii/leetcode/pull/14/files
本題ではないが, pythonのsortedとlist.sort()の計算中に空間計算量O(n)を消費する情報を得られてラッキー

numpy実装も確認したが,,,python側から見えるのはnp.arrayが実装されている前提のものだった
https://github.com/numpy/numpy/blob/v2.0.0/numpy/lib/_arraysetops_impl.py#L578-L668
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# sortを用いて
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        intersection_of_the_two = []
        seen = set()
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                if nums1[i1] not in seen:
                    intersection_of_the_two.append(nums1[i1])
                    seen.add(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return intersection_of_the_two
