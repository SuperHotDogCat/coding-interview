# hroc135: https://github.com/hroc135/leetcode/pull/27/files
# lower_bound, upper_boundとして名前を採用, 末尾最適化の話を一応確認, やはりMIN, MAXのマジックナンバーはよくなかったかと思い, NULLの時も考慮した比較関数isWithinIntervalを用意
# isValidChildなども名前の候補にあがったけどisValidHelperと紛らわしくタイポが発生したのでやめた
# goto-untrapped: https://github.com/goto-untrapped/Arai60/pull/52/files
# fhiyo: https://github.com/fhiyo/leetcode/pull/30/files 
# inorderでやる方法, アルゴリズムイントロダクションでもやったので真っ先に思い浮かんだが親のポインタがないので面倒だなと思っていたがyieldを使えばいいことを学ぶ
# あとはnode.valをif文の左側にもってくるなどの修正を加えるなど

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidHelper(root, None, None)

    def isValidHelper(self, node: Optional[TreeNode], lower_bound: Optional[int], upper_bound: Optional[int]) -> bool:
        # lower_bound, upper_boundは子に対する制約 lower_bound <= node.child.val <= upper_boundであることを課す
        # lower_bound, upper_boundは親の値によってきまる
        if node.left and node.right:
            if not self.isWithinInterval(node.left, lower_bound, upper_bound) or not self.isWithinInterval(node.right, lower_bound, upper_bound):
                return False
            if node.left.val < node.val < node.right.val:
                return self.isValidHelper(node.left, lower_bound, node.val) and self.isValidHelper(node.right, node.val, upper_bound)
            return False
        
        if node.left:
            if not self.isWithinInterval(node.left, lower_bound, upper_bound):
                return False
            if node.val > node.left.val:
                return self.isValidHelper(node.left, lower_bound, node.val)
            return False
        
        if node.right:
            if not self.isWithinInterval(node.right, lower_bound, upper_bound):
                return False
            if node.val < node.right.val:
                return self.isValidHelper(node.right, node.val, upper_bound)
            return False
        # ここまで到達すると葉ノードであることを示す
        return True
    
    def isWithinInterval(self, node: TreeNode, lower_bound: Optional[int], upper_bound: Optional[int]) -> bool:
        if lower_bound and upper_bound:
            return lower_bound < node.val < upper_bound
        
        if lower_bound:
            return node.val > lower_bound
        
        if upper_bound:
            return node.val < upper_bound
        # root nodeの場合
        return True

# yieldを使ったinorder
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def generate_node_inorder(node):
            if not node:
                return
            yield from generate_node_inorder(node.left)
            yield node
            yield from generate_node_inorder(node.right)
        # inorderで探索してソートされていなかったら二分木ではない
        prev_val = None
        for node in generate_node_inorder(root):
            if prev_val is not None and prev_val >= node.val:
                return False
            prev_val = node.val
        return True