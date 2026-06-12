# Problem: Find Minimum in Rotated Sorted Array
# Number: 153
# Difficulty: Medium
# URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 14.07 MB

class Solution {class Solution {
public:public:
    int findMin(vector<int>& nums) {    int findMin(vector<int>& nums) {
        int l = 0;        int l = 0;
        int r = nums.size() - 1;        int r = nums.size() - 1;

        while (l < r) {        while (l < r) {
            int mid = (l + r) / 2;            int mid = (l + r) / 2;
        }        }
            if (nums[r] < value) {            if (nums[r] < value) {
            int value = nums[mid];            int value = nums[mid];

                l = mid + 1;                l = mid + 1;
            } else {            } else {
                r = mid;                r = mid;
            }            }
    }    }

        return nums[l];        return nums[l];
};};
