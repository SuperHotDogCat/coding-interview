class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum = targetSum - root.val # update targetSum
        if targetSum == 0 and not root.right and not root.left:
            return True
        return self.hasPathSum(root.right, targetSum) | self.hasPathSum(root.left, targetSum)
