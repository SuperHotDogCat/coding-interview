# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, None, None)

    def isValidBSTHelper(self, node: Optional[TreeNode], lower_bound: Optional[TreeNode], upper_bound: Optional[TreeNode]) -> bool:
        if not node:
            return True

        if not self.isWithinIntervals(node, lower_bound, upper_bound):
            return False
        
        return self.isValidBSTHelper(node.left, lower_bound, node.val) and self.isValidBSTHelper(node.right, node.val, upper_bound)
    
    def isWithinIntervals(self, node: TreeNode, lower_bound: Optional[TreeNode], upper_bound: Optional[TreeNode]) -> bool:
        if lower_bound and upper_bound:
            return lower_bound < node.val < upper_bound
        
        if lower_bound is not None:
            return node.val > lower_bound
        
        if upper_bound is not None:
            return node.val < upper_bound
        
        return True
