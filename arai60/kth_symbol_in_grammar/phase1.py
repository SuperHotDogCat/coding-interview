class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        moves = deque([]) # 0: move left 1: move right
        # store the order from the leaf
        for i in range(n-1):
            if (k - 1) % 2 == 0:
                moves.appendleft(0)
            else:
                moves.appendleft(1)
            k = (k - 1) // 2 # 0-indexed 
            k += 1 # 1-indexed 
        kth_symbol = 0
        for move in moves:
            # move 0 kth_symbol 0 -> 0
            # move 1 kth_symbol 0 -> 1
            # move 0 kth_symbol 1 -> 1
            # move 1 kth_symbol 1 -> 0
            kth_symbol = kth_symbol ^ move
        
        return kth_symbol