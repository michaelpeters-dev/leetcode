# Problem: Trapping Rain Water
# Number: 42
# Difficulty: Hard
# URL: https://leetcode.com/problems/trapping-rain-water/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution {class Solution {
public:public:
    int trap(vector<int>& height) {    int trap(vector<int>& height) {
        int l = 0;        int l = 0;

        int total = 0;        int total = 0;
        while (l < r) {        while (l < r) {
        }        }
            if (maxLeft <= maxRight) {            if (maxLeft <= maxRight) {
            } else {            } else {
                total += maxLeft - height[l];                total += maxLeft - height[l];
                l++;                l++;
                total += maxRight - height[r];                total += maxRight - height[r];
            }            }
                r--;                r--;

        int maxLeft = height[l];        int maxLeft = height[l];
        int r = height.size() - 1;        int r = height.size() - 1;
        int maxRight = height[r];        int maxRight = height[r];
            maxLeft = max(maxLeft, height[l]);            maxLeft = max(maxLeft, height[l]);
            maxRight = max(maxRight, height[r]);            maxRight = max(maxRight, height[r]);
