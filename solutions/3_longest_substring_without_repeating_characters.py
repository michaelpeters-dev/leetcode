# Problem: Longest Substring Without Repeating Characters
# Number: 3
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    int lengthOfLongestSubstring(string s) {    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> counter;        unordered_map<char, int> counter;
        unordered_set<char> present;        unordered_set<char> present;

        int trail = 0;        int trail = 0;
        int longest = 0;        int longest = 0;

        for (int i = 0; i < s.length(); i++) {        for (int i = 0; i < s.length(); i++) {
    }    }
            char temp = s[i];            char temp = s[i];

            while (present.count(temp)) {            while (present.count(temp)) {
                counter[s[temp]]--;                counter[s[temp]]--;
            }            }
                present.erase(s[trail]);                present.erase(s[trail]);
                trail++;                trail++;
        }        }

            present.insert(temp);            present.insert(temp);
            counter[temp]++;            counter[temp]++;
            longest = max(longest, i - trail + 1);            longest = max(longest, i - trail + 1);

        return longest;        return longest;
};};
