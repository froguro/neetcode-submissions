/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int res = INT_MIN;
        dfs(root, res);
        return res;
    }
private:
    int dfs(TreeNode* curr, int& res) {
        if (!curr) {
            return 0;
        }
        int leftMax = max(0, dfs(curr->left, res));
        int rightMax = max(0, dfs(curr->right, res));
        int currMax = leftMax + rightMax + curr->val;
        res = max(res, currMax);

        return max(leftMax, rightMax) + curr->val;
    }
};
