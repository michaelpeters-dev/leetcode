# Problem: Longest Consecutive Sequence
# Number: 128
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Submission Status: Accepted
# Runtime: 86 ms
# Memory: 26.80 MB

        """        """
        :type nums: List[int]        :type nums: List[int]
        :rtype: int        :rtype: int
        """        """
        store = set()        store = set()

        for num in nums:        for num in nums:
            store.add(num)            store.add(num)
                
        for num in store:        for num in store:
            if num-1 in store:            if num-1 in store:
                continue                continue
            else:            else:
        largest = 0        largest = 0
            temp = 0            temp = 0
                while num in store:                while num in store:
                    temp += 1                    temp += 1
                    num += 1                    num += 1
                    largest = max(largest, temp)                    largest = max(largest, temp)
        return largest        return largest
                
