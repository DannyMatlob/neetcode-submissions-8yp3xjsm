# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getHeight(root: Optional[TreeNode]) -> int:
            if root is None: return 0
            leftHeight = getHeight(root.left)
            rightHeight = getHeight(root.right)
            curDiam = leftHeight + rightHeight

            self.diameter = max(curDiam, self.diameter)
            return 1 + max(leftHeight, rightHeight)
        
        self.diameter = 0

        getHeight(root)

        return self.diameter

        