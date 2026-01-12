# Problem: Product of Array Except Self
# Number: 238
# Difficulty: Medium
# URL: https://leetcode.com/problems/product-of-array-except-self/
# Submission Status: Accepted
# Runtime: 23 ms
# Memory: 25.68 MB

    def productExceptSelf(self, nums: List[int]) -> List[int]:    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prevL = 1        prevL = 1
        prevR = 1        prevR = 1
        res = [1] * len(nums)        res = [1] * len(nums)

        L = 0        L = 0
        R = len(nums) - 1        R = len(nums) - 1
        while L<len(nums):        while L<len(nums):
            res[L] *= prevL            res[L] *= prevL
            res[R] *= prevR            res[R] *= prevR
            prevL = nums[L] * prevL            prevL = nums[L] * prevL
            prevR = nums[R] * prevR            prevR = nums[R] * prevR
                        
            L += 1            L += 1
            R -= 1            R -= 1
        return res        return res
