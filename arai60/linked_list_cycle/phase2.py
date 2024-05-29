"""
Reference:
goto-untrappedさん: https://github.com/goto-untrapped/Arai60/pull/21/files
NobukiFukuiさん: 
hayashi-ayさん: https://github.com/hayashi-ay/leetcode/pull/15/files

phase1でsetを使うことに少し躊躇いがありました。LinkedListにhashableなのか気になったからです。
調べたところ, __hash__()はカスタムなハッシュ値を使いたい人向けのメソッドだそうです。
(でも本当に実行中hash値が変化していないのかは意識はした方が良いかもですね)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set([])
        node = head
        while node:
            if node in seen:
                return True
            seen.add(node) # store the visited node
            node = node.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle-finding algorithm
        slow = head
        fast = head
        while  fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
