# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parentMap = {None:None}
        nodeMap = {0:None}
        def dfs(node,parent):
            if not node:
                return
            nodeMap[node.val] = node
            parentMap[node] = parent
            dfs(node.left,node)
            dfs(node.right,node)
        
        dfs(root,None)

        q = deque([nodeMap[start]])
        vis = set([nodeMap[start]])
        t = -1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in (node.left,node.right,parentMap[node]):
                    if nei and nei not in vis:
                        q.append(nei)
                        vis.add(nei)
            t+=1
        
        return t
