class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_max, left_min = self.subtreeMinMax(root.left)
        right_max, right_min = self.subtreeMinMax(root.right)

        if left_max is not None and left_max >= root.val:
            return False
        if right_min is not None and right_min <= root.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
    
    @cache
    def subtreeMinMax(self, node: Optional[TreeNode]) -> Tuple[Optional[int], Optional[int]]:
        if not node:
            return None, None

        left_max, left_min = self.subtreeMinMax(node.left)
        right_max, right_min = self.subtreeMinMax(node.right)

        if left_max is not None and right_max is not None:
            return max(node.val, left_max, right_max), min(node.val, left_min, right_min)
        if left_max is not None:
            return max(node.val, left_max), min(node.val, left_min)
        if right_max is not None:
            return max(node.val, right_max), min(node.val, right_min)

        return node.val, node.val
