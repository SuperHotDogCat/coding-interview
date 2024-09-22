"""
Stack overflowしないかの一応の考察, height-balancedなので偏りがなく, 木の高さはlogn程度なので再帰の呼び出しは大丈夫そう
時間計算量考察: ざっくりとT(n)=2T(n/2)の漸化式が建てられるのでT(n)=O(n)
seal-azarashiさん: https://github.com/seal-azarashi/leetcode/pull/23/files 
    Phase1で書いたときの引数に配列のcopyを渡していたがコピーコストがかかることを考えて, indexで調べる区間を調整した方が良さそう。
Ryotaro25さん: https://github.com/Ryotaro25/leetcode_first60/pull/26
TORUS0818さん: https://github.com/TORUS0818/leetcode/pull/26
sakupan102さん: https://github.com/sakupan102/arai60-practice/pull/25
kazukiiiさん: https://github.com/kazukiii/leetcode/pull/25

[left, right)区間で構成する
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(left, right):
            if left >= right:
                return None
            mid = (right + left) // 2
            node = TreeNode(nums[mid])
            node.left = build_bst(left, mid)
            node.right = build_bst(mid+1, right)
            return node

        return build_bst(0, len(nums))
