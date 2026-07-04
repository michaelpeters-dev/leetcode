# Problem: Count Good Nodes in Binary Tree
# Number: 1448
# Difficulty: Medium
# URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {} *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * }; * };
 */ */
class Solution {class Solution {
public:public:
    int dfs(TreeNode* node, int msf) {    int dfs(TreeNode* node, int msf) {
    }    }
        if (node == nullptr) {        if (node == nullptr) {
            return 0;            return 0;
        }        }

        if (node->val >= msf) {        if (node->val >= msf) {
        }        }

    int goodNodes(TreeNode* root) {    int goodNodes(TreeNode* root) {
        int good = 0;        int good = 0;
            good++;            good++;
        msf = max(node->val, msf);        msf = max(node->val, msf);

        return good + dfs(node->left, msf) + dfs(node->right, msf);        return good + dfs(node->left, msf) + dfs(node->right, msf);
    }    }
        return dfs(root, root->val);        return dfs(root, root->val);
};};
