# Problem: Permutation in String
# Number: 567
# Difficulty: Medium
# URL: https://leetcode.com/problems/permutation-in-string/
# Submission Status: Accepted
# Runtime: 8 ms
# Memory: 10.77 MB

class Solution {class Solution {
public:public:
    bool checkInclusion(string s1, string s2) {    bool checkInclusion(string s1, string s2) {
        if (s2.size() < s1.size()) {        if (s2.size() < s1.size()) {
        unordered_map<char, int> first;        unordered_map<char, int> first;
        unordered_map<char, int> second;        unordered_map<char, int> second;

            return false;            return false;
        }        }

        for (int i = s1.size(); i < s2.size(); i++) {        for (int i = s1.size(); i < s2.size(); i++) {
    }    }
        }        }
        for (int i = 0; i < s1.size(); i++) {        for (int i = 0; i < s1.size(); i++) {

            first[s1[i]]++;            first[s1[i]]++;
        }        }
            second[s2[i]]++;            second[s2[i]]++;
            second[s2[i]]++;            second[s2[i]]++;
            second[s2[i-s1.size()]]--;            second[s2[i-s1.size()]]--;

            if (second[s2[i-s1.size()]]==0) {            if (second[s2[i-s1.size()]]==0) {
                second.erase(s2[i-s1.size()]);                second.erase(s2[i-s1.size()]);
            }            }

            if (first==second) {            if (first==second) {
                return true;                return true;
            }            }
        return false;        return false;


        if (first==second) return true;        if (first==second) return true;
};};
