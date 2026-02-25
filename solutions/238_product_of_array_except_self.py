# Problem: Product of Array Except Self
# Number: 238
# Difficulty: Medium
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        for (auto num: backward) {        for (auto num: backward) {
            cout << num << " ";            cout << num << " ";
        }        }

        vector<int> ans(nums.size());        vector<int> ans(nums.size());
        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
            ans[i] = forward[i] * backward[i];            ans[i] = forward[i] * backward[i];
        }        }
        return ans;        return ans;
    }    }
                
};};
