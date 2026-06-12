# Problem: Search in Rotated Sorted Array
# Number: 33
# Difficulty: Medium
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 15.28 MB

            int mid = (l + r) / 2;            int mid = (l + r) / 2;
            if (nums[mid] > nums[r]) {             if (nums[mid] > nums[r]) { 
                l = mid + 1;                l = mid + 1;
            } else {            } else {
                r = mid;                r = mid;
            }            }
        }        }

        int pivot = l;        int pivot = l;
                
        l = pivot;        l = pivot;
        r = nums.size() + pivot - 1;        r = nums.size() + pivot - 1;
        while (l <= r) {        while (l <= r) {
            int fakeMid = (l + r)/2;            int fakeMid = (l + r)/2;
            int realMid = fakeMid % nums.size();            int realMid = fakeMid % nums.size();
            int value = nums[realMid];            int value = nums[realMid];
            if (value < target) {            if (value < target) {
                l = fakeMid + 1;                l = fakeMid + 1;
            } else if (value > target) {            } else if (value > target) {
                r = fakeMid - 1;                r = fakeMid - 1;
            } else {            } else {
                return realMid;                return realMid;
            }            }
        }        }

        return -1;        return -1;
