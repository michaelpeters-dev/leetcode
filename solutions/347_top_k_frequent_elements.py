# Problem: Top K Frequent Elements
# Number: 347
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submission Status: Accepted
# Runtime: 11 ms
# Memory: 21.00 MB

        if k == 0:        if k == 0:
            return 0            return 0

        temp = {}        temp = {}
        for i in range(len(nums)):        for i in range(len(nums)):
            temp[nums[i]] = temp.get(nums[i], 0) + 1            temp[nums[i]] = temp.get(nums[i], 0) + 1
        print(temp)        print(temp)

        sorted_items = sorted(temp.items(), key = lambda item:item[1], reverse=True)        sorted_items = sorted(temp.items(), key = lambda item:item[1], reverse=True)
                
        res = []        res = []
        for j in range(k):        for j in range(k):
            res.append(sorted_items[j][0])            res.append(sorted_items[j][0])
        print(sorted_items)        print(sorted_items)
        return res        return res
