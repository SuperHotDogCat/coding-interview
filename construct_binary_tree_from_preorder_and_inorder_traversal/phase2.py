# olsen-blue: https://github.com/olsen-blue/Arai60/pull/29/files
    # preorderの呼び出され方を考えると副作用のある関数を許せば関数が呼び出されるたびにpreorderのindexを1つ進めるだけでよくなる, スライス操作の方は確かにphase1でも書いたが個人的にも速度とかの低下が怖い
# hroc135: https://github.com/hroc135/leetcode/pull/28/files 
# kazukiii: https://github.com/kazukiii/leetcode/pull/30/files
# seal-azarashi: https://github.com/seal-azarashi/leetcode/pull/29#discussion_r1813998042
# nittoco: https://github.com/nittoco/leetcode/pull/37/files

# 副作用のあるhelper関数を許す
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = -1
        def build_tree_helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            nonlocal preorder_index
            preorder_index += 1
            node = TreeNode(preorder[preorder_index])
            inorder_split_index = inorder.index(preorder[preorder_index]) # ここの行をmapにすると速くはなる
            node.left = build_tree_helper(left, inorder_split_index - 1)
            node.right = build_tree_helper(inorder_split_index + 1, right)
            return node

        return build_tree_helper(0, len(preorder) - 1)

# 範囲情報を入れてpreorder順に見ていく場合の実装(参考: https://github.com/nittoco/leetcode/pull/37/files)
from dataclasses import dataclass

@dataclass
class InorderPosition:
    node: TreeNode
    left_limit: int
    right_limit: int

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dummy = TreeNode()
        stack = [InorderPosition(dummy, inf, inf)]
        node_val_to_inorder_index = {val: i for i, val in enumerate(inorder)}
        for node_id in preorder:
            inorder_split_index = node_val_to_inorder_index[node_id]
            node = TreeNode(node_id) 
            back = stack[-1]
            if inorder_split_index < back.left_limit:
                back.node.left = node
                stack.append(InorderPosition(node, inorder_split_index, back.left_limit))
                continue
            back = self.search_parent_of_right_child(inorder_split_index, stack)
            back.node.right = node
            stack.append(InorderPosition(node, inorder_split_index, back.right_limit))
        return dummy.left

    def search_parent_of_right_child(self, inorder_split_index: int, stack: list[InorderPosition]) -> InorderPosition:
        while stack:
            if inorder_split_index < stack[-1].right_limit:
                return stack[-1]
            stack.pop()
