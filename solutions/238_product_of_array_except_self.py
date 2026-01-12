# Problem: Product of Array Except Self
# Number: 238
# Difficulty: Medium
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        for i in range(1, len(nums)):        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]            left[i] = left[i - 1] * nums[i - 1]
        print(left)        print(left)

        for i in range(len(nums) - 2, 0, -1):        for i in range(len(nums) - 2, 0, -1):
            right[i] = right[i + 1]  * nums[i + 1]            right[i] = right[i + 1]  * nums[i + 1]
        print(right)        print(right)

        res = [1] * (len(nums) - 2)        res = [1] * (len(nums) - 2)
        for i in range(1, len(nums)-1):        for i in range(1, len(nums)-1):
            res[i-1] = left[i] * right[i]            res[i-1] = left[i] * right[i]
        print(res)        print(res)
        return res        return res

