/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int result;
    public int goodNodes(TreeNode root) {
        result = 0;
        dfs(root, -101);
        return result;
    }

    public void dfs(TreeNode node, int max) {
        if (node == null) return;
        int newMax = max;
        if (node.val >= max) {
            newMax = node.val;
            result++;
        }

        dfs(node.left, newMax);
        dfs(node.right, newMax);
    }
}
