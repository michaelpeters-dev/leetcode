# Problem: Kth Largest Element in a Stream
# Number: 703
# Difficulty: Easy
# URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

class KthLargest:class KthLargest:

    def __init__(self, k: int, nums: List[int]):    def __init__(self, k: int, nums: List[int]):
        self.k = k        self.k = k

    def add(self, val: int) -> int:    def add(self, val: int) -> int:
        self.nums.append(val)        self.nums.append(val)


# Your KthLargest object will be instantiated and called as such:# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)# obj = KthLargest(k, nums)
        self.nums = nums        self.nums = nums
        self.nums.sort(reverse=True)        self.nums.sort(reverse=True)
        return self.nums[self.k-1]        return self.nums[self.k-1]
# param_1 = obj.add(val)# param_1 = obj.add(val)
