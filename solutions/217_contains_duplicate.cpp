// Problem:    217. Contains Duplicate
// Difficulty: Easy
// Language:   C++
// Runtime:    63 ms
// Memory:     111.4 MB
// Solved:     2026-10-08
// URL:        https://leetcode.com/problems/contains-duplicate/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> store;
        for (const auto& num: nums) {
            if (store.contains(num)) {
                return true;
            }
            store.insert(num);
        }
        return false;
    }
};
