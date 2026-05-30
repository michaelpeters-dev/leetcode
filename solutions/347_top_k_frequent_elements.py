# Problem: Top K Frequent Elements
# Number: 347
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        unordered_map<int, vector<int>> mappings; // Storing in the form: {Frequency, number}        unordered_map<int, vector<int>> mappings; // Storing in the form: {Frequency, number}
        for (int i = 0; i < nums.size(); i++) {        for (int i = 0; i < nums.size(); i++) {
            mappings[i] = {};            mappings[i] = {};
        }        }

        // Looping through the counter numbers and reading them into the mappings        // Looping through the counter numbers and reading them into the mappings
        for (auto& num: counter) {        for (auto& num: counter) {
            mappings[num.second].push_back(num.first);            mappings[num.second].push_back(num.first);
        }        }

        for (int i = nums.size(); i>0; i--) {        for (int i = nums.size(); i>0; i--) {
        // Looping in descending order and reading the result in        // Looping in descending order and reading the result in
        vector<int> result;        vector<int> result;
            for (auto& num: mappings[i]) {            for (auto& num: mappings[i]) {
        }        }
                result.push_back(num);                result.push_back(num);
            }            }
                if (result.size() == k) {                if (result.size() == k) {
                    return result;                    return result;
                }                }

        }        }
            counter[num]++;            counter[num]++;
        for (auto& num: nums) {        for (auto& num: nums) {
        unordered_map<int, int> counter; // Storing in the form: {Number: Count}        unordered_map<int, int> counter; // Storing in the form: {Number: Count}
    vector<int> topKFrequent(vector<int>& nums, int k) {    vector<int> topKFrequent(vector<int>& nums, int k) {
public:public:
class Solution {class Solution {
