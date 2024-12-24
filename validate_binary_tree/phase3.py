class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, None, None)

    def isValidBSTHelper(self, node: Optional[TreeNode], lower_bound: Optional[TreeNode], upper_bound: Optional[TreeNode]) -> bool:
        if node.left and node.right:
            if not self.isWithinIntervals(node.left, lower_bound, upper_bound) or not self.isWithinIntervals(node.right, lower_bound, upper_bound):
                return False
            if node.left.val < node.val < node.right.val:
                return self.isValidBSTHelper(node.left, lower_bound, node.val) and self.isValidBSTHelper(node.right, node.val, upper_bound)
            return False
        if node.left:
            if not self.isWithinIntervals(node.left, lower_bound, upper_bound):
                return False
            if node.val > node.left.val:
                return self.isValidBSTHelper(node.left, lower_bound, node.val)
            return False
        
        if node.right:
            if not self.isWithinIntervals(node.right, lower_bound, upper_bound):
                return False
            if node.val < node.right.val:
                return self.isValidBSTHelper(node.right, node.val, upper_bound)
            return False
        # 葉ノードの場合
        return True
    
    def isWithinIntervals(self, node: TreeNode, lower_bound: Optional[TreeNode], upper_bound: Optional[TreeNode]) -> bool:
        if lower_bound and upper_bound:
            return lower_bound < node.val < upper_bound
        
        if lower_bound:
            return node.val > lower_bound
        
        if upper_bound:
            return node.val < upper_bound
        
        return True
