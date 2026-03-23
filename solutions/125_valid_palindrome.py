# Problem: Valid Palindrome
# Number: 125
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-palindrome/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 9.98 MB

        int R = s.size() - 1;        int R = s.size() - 1;
        int L = 0;        int L = 0;
        while (L <= R) {        while (L <= R) {
            if (!isalnum(s[L])) {            if (!isalnum(s[L])) {
                L++;                L++;
            }            }
                continue;                continue;
            if (!isalnum(s[R])) {            if (!isalnum(s[R])) {
                R--;                R--;
                continue;                continue;
            }            }

            if (toupper(s[L]) != toupper(s[R])) {            if (toupper(s[L]) != toupper(s[R])) {
            }            }
        }        }
            L++;            L++;
            R--;            R--;
                return false;                return false;
class Solution {class Solution {
public:public:
    bool isPalindrome(string s) {    bool isPalindrome(string s) {
        return true;        return true;
    }    }
};};
