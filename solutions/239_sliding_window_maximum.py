# Problem: Sliding Window Maximum
# Number: 239
# Difficulty: Hard
# URL: https://leetcode.com/problems/sliding-window-maximum/
# Submission Status: Accepted
# Runtime: 200 ms
# Memory: 34.91 MB

        q = collections.deque() # Contains indices        q = collections.deque() # Contains indices
        l = r = 0        l = r = 0

        while r < len(nums):        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:            while q and nums[q[-1]] < nums[r]:
            q.append(r)            q.append(r)
                q.pop()                q.pop()

            # remove left val from window            # remove left val from window
            if l > q[0]:            if l > q[0]:
                q.popleft()                q.popleft()
                        
            if (r + 1) >= k:            if (r + 1) >= k:
                output.append(nums[q[0]])                output.append(nums[q[0]])
            r += 1            r += 1
                l += 1                l += 1
        return output        return output
