# Problem: Minimum Window Substring
# Number: 76
# Difficulty: Hard
# URL: https://leetcode.com/problems/minimum-window-substring/
# Submission Status: Accepted
# Runtime: 19 ms
# Memory: 11.60 MB

class Solution {class Solution {
public:public:
    string minWindow(string s, string t) {    string minWindow(string s, string t) {
        if (t.empty() || s.empty()) return "";        if (t.empty() || s.empty()) return "";

        unordered_map<char, int> need;        unordered_map<char, int> need;
        for (char& c: t) need[c]++l        for (char& c: t) need[c]++l

        int required = need.size();        int required = need.size();
        int formed = 0;        int formed = 0;

        unordered_map<char, int> window;        unordered_map<char, int> window;
        int left = 0, right = 0;        int left = 0, right = 0;
        return minLen == INT_MAX ? "" : s.substr(start, minLen);        return minLen == INT_MAX ? "" : s.substr(start, minLen);

        int minLen = INT_MAX;        int minLen = INT_MAX;
        int start = 0;        int start = 0;

        while (right < s.size()) {        while (right < s.size()) {
            char c = s[right];            char c = s[right];
            window[c]++;            window[c]++;

            if (need.count(c) && window[c] == need[c]) {            if (need.count(c) && window[c] == need[c]) {
                formed++;                formed++;
            }            }

            while (left <= right && formed == required) {            while (left <= right && formed == required) {
                if (right - left + 1 < minLen) {                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;                    minLen = right - left + 1;
                }                }
            }            }
                    start = left;                    start = left;

                char ch = s[left];                char ch = s[left];
                window[ch]--;                window[ch]--;

                if (need.count(ch) && window[ch] < need[ch]) {                if (need.count(ch) && window[ch] < need[ch]) {
                    formed--;                    formed--;
                }                }
                left++;                left++;
            right++;            right++;
        }        }
    }    }
};};
