from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        last_seen_open_brankets = deque([])
        last_seen_open_branket = ""
        open_brankets = set(["(", "[", "{"])
        close_branket_to_open_branket = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in open_brankets:
                last_seen_open_brankets.appendleft(last_seen_open_branket)
                last_seen_open_branket = char
            
            elif char in close_branket_to_open_branket:
                if last_seen_open_branket != close_branket_to_open_branket[char]:
                    return False
                if len(last_seen_open_brankets) != 0:
                    last_seen_open_branket = last_seen_open_brankets.popleft()

        if len(last_seen_open_brankets) != 0:
            return False
        
        return True