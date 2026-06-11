# Problem: Binary Search
# Number: 704
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-search/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    int search(vector<int>& nums, int target) {    int search(vector<int>& nums, int target) {
        int l = 0;        int l = 0;
        int r = nums.size() - 1;        int r = nums.size() - 1;

        while (l <= r) {        while (l <= r) {
            int mid = (l + r) / 2;            int mid = (l + r) / 2;
        }        }
            if (nums[mid] == target) {            if (nums[mid] == target) {
                return mid;                return mid;
            } else if (nums[mid] < target) {            } else if (nums[mid] < target) {
                l = mid + 1;                l = mid + 1;
            } else {            } else {
                r = mid - ;                r = mid - ;
            }            }
    }    }

        return -1;        return -1;
};};
