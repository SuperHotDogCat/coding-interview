class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(left, right):
            if left >= right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = build_bst(left, mid)
            node.right = build_bst(mid+1, right)
            return node
        
        return build_bst(0, len(nums))
