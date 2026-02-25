# Problem: Two Sum
# Number: 1
# Difficulty: Easy
# URL: https://leetcode.com/problems/two-sum/
# Submission Status: Accepted
# Runtime: 3 ms
# Memory: 14.74 MB

class Solution {class Solution {
public:public:
    vector<int> twoSum(vector<int>& nums, int target) {    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> store;        unordered_map<int, int> store;
        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];            int need = target - nums[i];
            if (store.count(need)) {            if (store.count(need)) {
        }        }
                return {store[need], i};                return {store[need], i};
            } else {            } else {
                store[nums[i]] = i;                store[nums[i]] = i;
            }            }
    }    }
        return {-1};        return {-1};
};};
