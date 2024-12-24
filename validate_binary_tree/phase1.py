# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# テストケースで親ノードが及ぼす制約を考慮できていなく弾かれる
# なんだか命名やら条件文の書き方が不安
# 空間計算量と時間計算量ともにノード数をNとしたときにO(N)
# 今回の最大ノード数は10^4なのでPythonの1秒間の実行数が10^7程度だった記憶があるので(間違ってたら指摘してください)10^-3秒程度で実行が終わる
# そういえば, 今回はスタックオーバーフローが起こらなかったが, Pythonのデフォルトでの最大再帰数を考えると最大ノード数は10^4なので片方に偏ったBinary Treeの場合再帰エラーがおきる

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # -2 ** 31 <= Node.val <= 2 ** 31 - 1なので開区間でとる
        MIN = -2 ** 31 - 1
        MAX = 2 ** 32
        return self.isValidHelper(root, MIN, MAX)

    def isValidHelper(self, node: Optional[TreeNode], left, right) -> bool:
        # left, rightは子に対する制約 left < node.child.val < rightであることを課す
        # left, rightは親の値によってきまる

        if node.left and node.right:
            if not (left < node.left.val < right and left < node.right.val < right):
                return False
            if node.left.val < node.val < node.right.val:
                return self.isValidHelper(node.left, left, node.val) and self.isValidHelper(node.right, node.val, right)
            return False
        
        if node.left:
            if not left < node.left.val < right:
                return False
            if node.left.val < node.val:
                return self.isValidHelper(node.left, left, node.val)
            return False
        
        if node.right:
            if not left < node.right.val < right:
                return False
            if node.val < node.right.val:
                return self.isValidHelper(node.right, node.val, right)
            return False

        # ここまで到達すると葉ノードであることを示す
        return True
