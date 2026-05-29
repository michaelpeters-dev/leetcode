# Problem: Contains Duplicate
# Number: 217
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    bool containsDuplicate(vector<int>& nums) {    bool containsDuplicate(vector<int>& nums) {
        for (auto& num: nums) {        for (auto& num: nums) {
        }        }

        return false;        return false;
        unordered_set<int> store;        unordered_set<int> store;
            if (store.count(num)) {            if (store.count(num)) {
                return true;                return true;
            } else {            } else {
                store.insert(num);                store.insert(num);
            }            }
    }    }
};};
