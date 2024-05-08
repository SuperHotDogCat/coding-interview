"""
Reference:
fhiyoさん: https://github.com/fhiyo/leetcode/pull/4/files
nittocoさん: https://github.com/nittoco/leetcode/pull/9/files
TORUさん: https://github.com/TORUS0818/leetcode/pull/6/files
phase1の回答は, skip_numberという状態変数を持って条件を制御していくやりかただったが, 状態変数の扱いが難しいものになる恐れがあると考えた。
あまり状態変数は持ちたくないものではあるので, 重複が見つかったらスキップというやり方を採用する。
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def skip_duplicate_nodes(node):
            while node.next and node.val == node.next.val:
                node = node.next
            return node
        dummy_head = ListNode(-1)
        current_node = dummy_head
        while head:
            if head.next and head.val == head.next.val:
                head = skip_duplicate_nodes(head)
            else:
                current_node.next = ListNode(head.val)
                current_node = current_node.next
            head = head.next
        return dummy_head.next