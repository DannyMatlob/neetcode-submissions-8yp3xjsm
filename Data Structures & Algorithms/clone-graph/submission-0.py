"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newNodeMap = {}
        def dfs(node: Optional['Node']):
            if node is None: return

            if node.val in newNodeMap:
                return newNodeMap[node.val]

            nodeCopy = Node(node.val)
            newNodeMap[node.val] = nodeCopy

            newNeighbors = []
            if node.neighbors:
                for neighbor in node.neighbors:
                    newNeighbors.append(dfs(neighbor))
            
            nodeCopy.neighbors = newNeighbors
            return nodeCopy
        return dfs(node)