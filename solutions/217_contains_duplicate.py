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
        bool flag = false;        bool flag = false;

        for (const auto& num: nums) {        for (const auto& num: nums) {
        unordered_set<int> seen;        unordered_set<int> seen;
            if (seen.count(num)) {            if (seen.count(num)) {
                return true;                return true;
            } else {            } else {
        }        }
                seen.insert(num);                seen.insert(num);
            }            }
    }    }

        return false;        return false;
};};
