from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parentMap = {}

        def dfs(node, parent):
            if not node:
                return
            parentMap[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        q = deque([target])
        vis = set([target])
        while q:
            if k == 0:
                return [node.val for node in  q]
            
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left,node.right,parentMap[node]):
                    if nei and nei not in vis:
                        q.append(nei)
                        vis.add(nei)
            
            k-=1
        
        return []