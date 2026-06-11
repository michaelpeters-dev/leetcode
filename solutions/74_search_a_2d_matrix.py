# Problem: Search a 2D Matrix
# Number: 74
# Difficulty: Medium
# URL: https://leetcode.com/problems/search-a-2d-matrix/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

class Solution {class Solution {
public:public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0;        int l = 0;
        int r = matrix.size() * matrix[0].size() - 1;        int r = matrix.size() * matrix[0].size() - 1;

        while (l <= r) {        while (l <= r) {
            int mid = (l + r) / 2;            int mid = (l + r) / 2;
        }        }
            int row = mid / matrix[0].size();            int row = mid / matrix[0].size();
            int col = mid % matrix[0].size();            int col = mid % matrix[0].size();

            if (num == target) {            if (num == target) {
            int num = matrix[row][col];            int num = matrix[row][col];
                return true;                return true;
            } else if (num < target) {            } else if (num < target) {
                l = mid + 1;                l = mid + 1;
            } else {            } else {
                r = mid - 1;                r = mid - 1;
            }            }

    }    }
        return false;        return false;
};};
