# Problem: Longest Substring Without Repeating Characters
# Number: 3
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Submission Status: Accepted
# Runtime: 22 ms
# Memory: 14.25 MB

class Solution {class Solution {
public:public:
    int lengthOfLongestSubstring(string s) {    int lengthOfLongestSubstring(string s) {
        int n = s.size();        int n = s.size();
        int l = 0;        int l = 0;
        int r = 0;        int r = 0;
        unordered_set<int> store;        unordered_set<int> store;

    }    }
        while (r < n) {        while (r < n) {
            while (store.count(s[r])) {            while (store.count(s[r])) {
        }        }
        int longest = 0;        int longest = 0;
                store.erase(s[l]);                store.erase(s[l]);
            }            }
                l++;                l++;

            store.insert(s[r]);            store.insert(s[r]);
            longest = max(longest, r - l);            longest = max(longest, r - l);
            r++;            r++;

        return longest + 1;        return longest + 1;
};};
