"""
Reference: 
Ryotaro25: https://github.com/Ryotaro25/leetcode_first60/pull/3/files phase1の新しくListNodeを制作して末端の値と等しくなければ飛ばすコードを真似して書いてみた
kagetora0924: https://github.com/kagetora0924/leetcode-grind/pull/6/files 自分のphase1の方が状態管理する変数が少なくて頭のメモリをあまり消費しなくて良い気がした
fhiyo: https://github.com/fhiyo/leetcode/pull/3/files 重複ノード削除を関数にしていた。自分のコードにもせめてコメントぐらいは書くべきだと思い追記
"""

# Ryotaroさんのコードを参考に制作, 新しくListNodeを作るやり方
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy_head = ListNode(-1)
        dummy_head.next = ListNode(head.val)
        sentinel = dummy_head.next
        head = head.next
        while head:
            if head.val != sentinel.val:
                sentinel.next = ListNode(head.val)
                sentinel = sentinel.next
            head = head.next
        return dummy_head.next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = head
        while head:
            while head.next and head.val == head.next.val:
                # reconnect listnodes in order to delete duplicate ones.
                head.next = head.next.next
            head = head.next
        return dummy_head
    
    