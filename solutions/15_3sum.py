# Problem: 3Sum
# Number: 15
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum/
# Submission Status: Accepted
# Runtime: 48 ms
# Memory: 28.99 MB

                    ans.push_back({nums[p], nums[l], nums[r]});                    ans.push_back({nums[p], nums[l], nums[r]});
                    l++;                    l++;
                    r--;                    r--;

                    while (l < r && nums[l]==nums[l-1]) l++;                    while (l < r && nums[l]==nums[l-1]) l++;
                    while (l < r && nums[r]==nums[r+1]) r--;                    while (l < r && nums[r]==nums[r+1]) r--;
                } else {                } else {
                } else if (sum < 0) {                } else if (sum < 0) {
                    l++;                    l++;
                if (sum > 0) {                if (sum > 0) {
                    r--;                    r--;
            while (l < r) {            while (l < r) {
                int sum = nums[l] + nums[r] + nums[p];                int sum = nums[l] + nums[r] + nums[p];

            int r = n - 1;            int r = n - 1;
            int l = p + 1;            int l = p + 1;
                }                }
            }            }
        }        }
        return ans;        return ans;
    }    }
};};

        for (int p = 0; p < n; p++) {        for (int p = 0; p < n; p++) {
            if (p>0 && nums[p]==nums[p-1]) continue;            if (p>0 && nums[p]==nums[p-1]) continue;

        sort(nums.begin(), nums.end());        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;        vector<vector<int>> ans;
