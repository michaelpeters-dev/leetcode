# Problem: Two Sum
# Number: 1
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    vector<int> twoSum(vector<int>& nums, int target) {    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> store;        unordered_map<int, int> store;
        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];            int num = nums[i];
            if (store.count(target - num)) {            if (store.count(target - num)) {
                return {store[target - num], i};                return {store[target - num], i};
            }            }
        }        }
        return {};        return {};
    }    }
            store[nums[i]] = i;            store[nums[i]] = i;
};};
