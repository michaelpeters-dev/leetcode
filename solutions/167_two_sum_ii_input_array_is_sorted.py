# Problem: Two Sum II - Input Array Is Sorted
# Number: 167
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 19.35 MB

class Solution {class Solution {
public:public:
    vector<int> twoSum(vector<int>& numbers, int target) {    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();        int n = numbers.size();

            int sum = numbers[l] + numbers[r];            int sum = numbers[l] + numbers[r];
        int l = 0;        int l = 0;
        int r = n - 1;        int r = n - 1;

        for (int i = 0; i < n - 1; i++){        for (int i = 0; i < n - 1; i++){
        }        }
            if (sum == target) {            if (sum == target) {
                return {l + 1, r + 1};                return {l + 1, r + 1};
            }            }
    }    }

            if (sum > target) r--;            if (sum > target) r--;
            if (sum < target) l++;            if (sum < target) l++;
        return {0};        return {0};
};};
