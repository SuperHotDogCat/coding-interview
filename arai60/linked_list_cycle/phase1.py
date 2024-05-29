# hash table ノード数をnとすると空間計算量O(n), 時間計算量もO(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set([])
        node = head
        while node:
            if node in seen:
                return True
            seen.add(node) 
            node = node.next
        return False

# Floyd's cycle-finding algorithm 空間計算量O(1), 時間計算量O(n)
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

# サイクルの先頭ノードを出力する
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle-finding algorithm
        slow = head
        fast = head
        while  fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                print(fast.val)
                return True
        return False
