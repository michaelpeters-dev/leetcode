# Problem: Contains Duplicate
# Number: 217
# Difficulty: Easy
# URL: https://leetcode.com/problems/contains-duplicate/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution {class Solution {
public:public:
    bool containsDuplicate(vector<int>& nums) {    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> store;        unordered_set<int> store;
        for (auto num: nums) {        for (auto num: nums) {
            if (store.count(num) > 0) {            if (store.count(num) > 0) {
                return true;                return true;
            }            }
        }        }
    }    }
            store.insert(num);            store.insert(num);
        return false;        return false;
};};
