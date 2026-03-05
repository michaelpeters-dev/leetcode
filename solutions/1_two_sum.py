# Problem: Two Sum
# Number: 1
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 14.74 MB

class Solution {class Solution {
public:public:
    vector<int> twoSum(vector<int>& nums, int target) {    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> store;        unordered_map<int, int> store;

        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
            int offset = target - nums[i];            int offset = target - nums[i];
        }        }
            if (store.count(offset)) {            if (store.count(offset)) {
                return {store[offset], i};                return {store[offset], i};
            }            }
    }    }
            store[nums[i]] = i;            store[nums[i]] = i;
        return {};        return {};
