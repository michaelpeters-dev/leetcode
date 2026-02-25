# Problem: Contains Duplicate
# Number: 217
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate/
# Submission Status: Accepted
# Runtime: 43 ms
# Memory: 90.83 MB

class Solution {class Solution {
public:public:
    bool containsDuplicate(vector<int>& nums) {    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> store;        unordered_set<int> store;
        for (auto num: nums) {        for (auto num: nums) {
            if (store.count(num)) {            if (store.count(num)) {
                return true;                return true;
            } else {            } else {
        }        }
                store.insert(num);                store.insert(num);
            }            }
    }    }
        return false;        return false;
};};
