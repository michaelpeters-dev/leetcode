# Problem: Container With Most Water
# Number: 11
# Difficulty: Medium
# URL: https://leetcode.com/problems/container-with-most-water/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class Solution {class Solution {
public:public:
    int maxArea(vector<int>& height) {    int maxArea(vector<int>& height) {
        int n = height.size();        int n = height.size();
        int l = 0;        int l = 0;
        int r = n - 1;        int r = n - 1;

        while (l < r) {        while (l < r) {
            int x = r - l;            int x = r - l;
            int y = min(height[l], height[r]);            int y = min(height[l], height[r]);
            int area = x * y;            int area = x * y;
            result = max(result, area);            result = max(result, area);
        int result = INT_MIN;        int result = INT_MIN;
        return result;        return result;
        }        }


            if (height[l]<height[r]) {            if (height[l]<height[r]) {
                l++;                l++;
            } else {            } else {
                r--;                r--;
            }            }
    }    }
};};
