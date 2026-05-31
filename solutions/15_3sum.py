# Problem: 3Sum
# Number: 15
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum/
# Submission Status: Accepted
# Runtime: 43 ms
# Memory: 29.21 MB

        vector<vector<int>> result;        vector<vector<int>> result;
        for (int i = 0; i < nums.size() - 2; i++) {        for (int i = 0; i < nums.size() - 2; i++) {
            if (i>0 && nums[i]==nums[i-1]) {            if (i>0 && nums[i]==nums[i-1]) {
                continue;                continue;
            }            }
            int left = i + 1;            int left = i + 1;
            int right = nums.size() - 1;            int right = nums.size() - 1;
            while (left < right) {            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];                int sum = nums[i] + nums[left] + nums[right];

                if (sum > 0) {                if (sum > 0) {
                    right--;                    right--;
                } else if (sum < 0) {                } else if (sum < 0) {
                    left++;                    left++;
                } else {                } else {
                    result.push_back({nums[i], nums[left], nums[right]});                    result.push_back({nums[i], nums[left], nums[right]});
                    left++;                    left++;
                    right--;                    right--;
                    while (left < right && nums[left]==nums[left - 1]) {                    while (left < right && nums[left]==nums[left - 1]) {
                        left++;                        left++;
                    }                    }

                    while (left < right && nums[right]==nums[right + 1]) {                    while (left < right && nums[right]==nums[right + 1]) {
                        right--;                        right--;
                    }                    }
                }                }
            }            }
        }        }
        return result;        return result;
    }    }
};};
