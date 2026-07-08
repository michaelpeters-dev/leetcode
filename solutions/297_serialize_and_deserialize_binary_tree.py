# Problem: Serialize and Deserialize Binary Tree
# Number: 297
# Difficulty: Hard
# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Submission Status: Accepted
# Runtime: 4 ms
# Memory: N/A

        return carry;        return carry;
    }    }

    TreeNode* dhelper(int& index, vector<string>& passIn) {    TreeNode* dhelper(int& index, vector<string>& passIn) {
        if (passIn[index] == "#") {        if (passIn[index] == "#") {
            index++;            index++;
            return nullptr;            return nullptr;
        }        }
                
        int num = stoi(passIn[index]);        int num = stoi(passIn[index]);
        TreeNode* curr = new TreeNode(num);        TreeNode* curr = new TreeNode(num);

        index++;        index++;
        curr->left = dhelper(index, passIn);        curr->left = dhelper(index, passIn);
        curr->right = dhelper(index, passIn);        curr->right = dhelper(index, passIn);

        return curr;        return curr;
    }    }

    // Decodes your encoded data to tree.    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {    TreeNode* deserialize(string data) {
        vector<string> passIn;        vector<string> passIn;
        stringstream ss(data);        stringstream ss(data);
