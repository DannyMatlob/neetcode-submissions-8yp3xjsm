# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    depthMap = {}
    maxDepth = -1
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root, 0)
        
        result = []
        for i in range(self.maxDepth + 1):
            print("Appending: ", self.depthMap[i])
            result.append(self.depthMap[i])
        return result
    
    def dfs(self, root: Optional[TreeNode], depth):
        if root is None: return
        print("Searching: ", root.val)
        self.depthMap[depth] = root.val
        self.maxDepth = max(self.maxDepth, depth)

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)