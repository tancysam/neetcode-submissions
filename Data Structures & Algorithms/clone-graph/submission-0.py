"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited = set()
        genClone = {}

        def dfs(node):
            if node in visited:
                return genClone[node]
                
            
            visited.add(node)

            clone = Node()
            clone.val = node.val
            genClone[node] = clone

            for n in node.neighbors:
                v = dfs(n)
                if v:
                    clone.neighbors.append(v)
            
            return clone

        if not node:
            return None
        elif len(node.neighbors) == 0:
            clone = Node()
            clone.val = node.val
            return clone

        return dfs(node)




            
            

            


