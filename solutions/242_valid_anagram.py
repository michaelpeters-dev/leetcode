# Problem: Valid Anagram
# Number: 242
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-anagram/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution {class Solution {
public:public:
    bool isAnagram(string s, string t) {    bool isAnagram(string s, string t) {
        unordered_map<char, int> sStore;        unordered_map<char, int> sStore;
        unordered_map<char, int> tStore;        unordered_map<char, int> tStore;

        if (s.length() != t.length()) {        if (s.length() != t.length()) {
            return false;            return false;
        }        }
    }    }

        for (int i = 0; i < s.length(); i++) {        for (int i = 0; i < s.length(); i++) {
            sStore[s[i]]++;            sStore[s[i]]++;
        }        }
            tStore[t[i]]++;            tStore[t[i]]++;

        return sStore == tStore;        return sStore == tStore;
};};
