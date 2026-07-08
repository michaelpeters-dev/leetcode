# Problem: Binary Tree Maximum Path Sum
# Number: 124
# Difficulty: Hard
# URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 27.80 MB

        if (node == nullptr) {        if (node == nullptr) {
        }        }
            return 0;            return 0;

        int leftMax = maximum(node->left);        int leftMax = maximum(node->left);
        int rightMax = maximum(node->right);        int rightMax = maximum(node->right);
                
        largest = max(largest, leftMax + rightMax + node->val);        largest = max(largest, leftMax + rightMax + node->val);
        largest = max(largest, leftMax + node->val);        largest = max(largest, leftMax + node->val);
        largest = max(largest, rightMax + node->val);        largest = max(largest, rightMax + node->val);
    int maximum(TreeNode* node) {    int maximum(TreeNode* node) {
    int largest;    int largest;
        largest = max(largest, node->val);        largest = max(largest, node->val);

        return max(node->val, max(node->val + leftMax, node->val + rightMax));        return max(node->val, max(node->val + leftMax, node->val + rightMax));
    }    }

    int maxPathSum(TreeNode* root) {    int maxPathSum(TreeNode* root) {
        largest = INT_MIN;        largest = INT_MIN;
        maximum(root);        maximum(root);
    }    }
        return largest;        return largest;
};};
