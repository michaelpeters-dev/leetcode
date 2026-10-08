// Problem:    242. Valid Anagram
// Difficulty: Easy
// Language:   C++
// Runtime:    3 ms
// Memory:     9.8 MB
// Solved:     2026-10-08
// URL:        https://leetcode.com/problems/valid-anagram/

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> first;
        unordered_map<char, int> second;

        for (const char& ch: s) {
            first[ch]++;
        }
        for (const char& ch: t) {
            second[ch]++;
        }

        return (first == second);
    }
};
