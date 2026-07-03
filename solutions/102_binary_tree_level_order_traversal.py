# Problem: Binary Tree Level Order Traversal
# Number: 102
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Submission Status: Accepted
# Runtime: 10 ms
# Memory: 17.08 MB

        queue<TreeNode*> q;        queue<TreeNode*> q;
        vector<vector<int>> result;        vector<vector<int>> result;

        while (!q.empty()) {        while (!q.empty()) {
        q.push(root);        q.push(root);
            vector<int> temp;            vector<int> temp;
            for (int i = 0; i < qLength; i++) {            for (int i = 0; i < qLength; i++) {
            int qLength = q.size();            int qLength = q.size();
                TreeNode* node = q.front(); q.pop();                TreeNode* node = q.front(); q.pop();
                if (node->left != nullptr) {                if (node->left != nullptr) {
                    q.push(node->left);                    q.push(node->left);
                }                }
                if (node->right != nullptr) {                if (node->right != nullptr) {
                    q.push(node->right);                    q.push(node->right);
                }                }

                temp.push_back(node->val);                temp.push_back(node->val);
            }            }
            result.push_back(temp);            result.push_back(temp);
        }        }

        return result;        return result;
    }    }
