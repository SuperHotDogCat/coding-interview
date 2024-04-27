# そういえばOdaさんに指摘される前の問題で、解き直しもしていなかったので, 
# 前のようにintとかstrを使わずにしっかり他人のコードを見て考えてみる

"""
Reference
sakupan-san https://github.com/sakupan102/arai60-practice/pull/6/files
デジタル回路の授業でやったキャリーアダーを連想しました。divmod関数も知らなかったです。
一旦計算してそのあと1の位, 10の位, ....という感じで取り出そうとしていたので考えが至らなかったです。

命名などを参考にしました。どのコードもsentinel.nextを出力していて, これは思いつかなかったです。
nittoco-san https://github.com/nittoco/leetcode/pull/2/files,yukimichishita-san https://github.com/YukiMichishita/LeetCode/pull/2#discussion_r1527644048
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        tail_node = sentinel
        carry = 0
        while l1 or l2 or carry:
            add_value = carry
            if l1:
                add_value += l1.val
                l1 = l1.next
            
            if l2:
                add_value += l2.val
                l2 = l2.next

            carry, digit = divmod(add_value, 10)
            tail_node.next = ListNode(digit)
            tail_node = tail_node.next
        return sentinel.next