# Problem: Two Sum II - Input Array Is Sorted
# Number: 167
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

    vector<int> twoSum(vector<int>& numbers, int target) {    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;        int l = 0;
        int r = numbers.size() - 1;        int r = numbers.size() - 1;

        while (l < r) {        while (l < r) {
            if (sum == target) {            if (sum == target) {
        }        }
            int sum = numbers[l] + numbers[r];            int sum = numbers[l] + numbers[r];
                return {l + 1, r + 1};                return {l + 1, r + 1};
            } else if (sum < target) {            } else if (sum < target) {
                l++;                l++;
            } else {            } else {
                r--;                r--;
            }            }

        return {};        return {};
    }    }
