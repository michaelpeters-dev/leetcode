# Problem: Construct Binary Tree from Preorder and Inorder Traversal
# Number: 105
# Difficulty: Medium
# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

        if (left > right) {        if (left > right) {
        }        }
            return nullptr;            return nullptr;

        TreeNode* root = new TreeNode(preorder[index]);        TreeNode* root = new TreeNode(preorder[index]);
        index++;        index++;

        int mid = left;        int mid = left;
        root->left = build(preorder, inorder, index, left, mid - 1);        root->left = build(preorder, inorder, index, left, mid - 1);
    }    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        root->right = build(preorder, inorder, index, mid + 1, right);        root->right = build(preorder, inorder, index, mid + 1, right);

        return root;        return root;
        while (inorder[mid] != root->val) {        while (inorder[mid] != root->val) {

            mid++;            mid++;
        }        }
        return build(preorder, inorder, index, 0, preorder.size() - 1);        return build(preorder, inorder, index, 0, preorder.size() - 1);
    }    }
        int index = 0;        int index = 0;
};};
