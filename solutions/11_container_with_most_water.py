# Problem: Container With Most Water
# Number: 11
# Difficulty: Medium
# URL: https://leetcode.com/problems/container-with-most-water/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    int maxArea(vector<int>& height) {    int maxArea(vector<int>& height) {
        int answer = 0;        int answer = 0;

        int l = 0;        int l = 0;
        int r = height.size() - 1;        int r = height.size() - 1;

        while (l < r) {        while (l < r) {
            int area = (r - l) * min(height[l], height[r]);            int area = (r - l) * min(height[l], height[r]);
        }        }
            answer = max(answer, area);            answer = max(answer, area);

            if (height[l] <= height[r]) {            if (height[l] <= height[r]) {
                l++;                l++;
            } else {            } else {
                r--;                r--;
            }            }
    }    }

        return answer;        return answer;
