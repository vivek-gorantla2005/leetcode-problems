from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
                
        visit = set(deadends)
        
        if "0000" in visit:
            return -1
        
        q = deque()
        q.append(("0000", 0))  
        visit.add("0000")

        while q:
            node, moves = q.popleft()
            
            if node == target:
                return moves

            for child in children(node):
                if child not in visit:  
                    visit.add(child)
                    q.append((child, moves + 1))
        
        return -1