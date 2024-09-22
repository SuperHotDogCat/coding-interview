# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        add_node = TreeNode(val=nums[len(nums)//2])
        add_node.left = self.sortedArrayToBST(nums[:len(nums)//2])
        add_node.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        return add_node
