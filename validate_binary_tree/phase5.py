class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_max, _ = self.subtreeMinMax(root.left)
        _, right_min = self.subtreeMinMax(root.right)

        if not (left_max < root.val < right_min):
            return False
    
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    
    @cache
    def subtreeMinMax(self, node: Optional[TreeNode]) -> Union[float, int]:
        # nodeを含む部分木のmin, maxを出力する
        if not node:
            return -math.inf, math.inf

        left_max, left_min = self.subtreeMinMax(node.left)
        right_max, right_min = self.subtreeMinMax(node.right)

        return max(node.val, left_max, right_max), min(node.val, left_min, right_min)
