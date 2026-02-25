# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 2 ms
# Memory: 9.89 MB

        unordered_map<char, int> second;        unordered_map<char, int> second;

        for (int i = 0; i < n; i++) {        for (int i = 0; i < n; i++) {
        int n = s.size();        int n = s.size();
            first[s[i]] += 1;            first[s[i]] += 1;
        }        }
            second[t[i]] += 1;            second[t[i]] += 1;
        unordered_map<char, int> first;        unordered_map<char, int> first;

        }        }
    bool isAnagram(string s, string t) {    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {        if (s.size() != t.size()) {
            return false;            return false;
public:public:
class Solution {class Solution {
