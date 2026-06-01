# Problem: Permutation in String
# Number: 567
# Difficulty: Medium
# URL: https://leetcode.com/problems/permutation-in-string/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    bool checkInclusion(string s1, string s2) {    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> standard;        unordered_map<char, int> standard;
        for (const auto& letter: s1) {        for (const auto& letter: s1) {
            standard[letter]++;            standard[letter]++;
        }        }

        for (int i = 0; i < s2.length(); i++) {        for (int i = 0; i < s2.length(); i++) {
            if (i<s1.length()) {            if (i<s1.length()) {
                store[s2[i]]++;                store[s2[i]]++;
            }            }
        unordered_map<char, int> store;        unordered_map<char, int> store;
                continue;                continue;

            if (store == standard) {            if (store == standard) {
                return true;                return true;
            }            }
            store[s2[i]]++;            store[s2[i]]++;
            store[s2[i - s1.length()]]--;            store[s2[i - s1.length()]]--;

        return false;        return false;
            if(store[s2[i - s1.length()]] == 0) {            if(store[s2[i - s1.length()]] == 0) {
        }        }
                store.erase(s2[i - s1.length()]);                store.erase(s2[i - s1.length()]);
            }            }
    }    }

        if (store == standard) return true;        if (store == standard) return true;
};};
