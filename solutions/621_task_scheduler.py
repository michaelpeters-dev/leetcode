# Problem: Task Scheduler
# Number: 621
# Difficulty: Medium
# URL: https://leetcode.com/problems/task-scheduler/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A


        time = 0        time = 0
        q = deque() # pairs of (-cnt, idleTime)        q = deque() # pairs of (-cnt, idleTime)

        while maxHeap or q:        while maxHeap or q:
            time += 1            time += 1
            if maxHeap:            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:                if cnt:
                    q.append([cnt, time + n])                    q.append([cnt, time + n])
            if q and q[0][1]==time:            if q and q[0][1]==time:
        heapq.heapify(maxHeap)        heapq.heapify(maxHeap)
        maxHeap = [-cnt for cnt in count.values()]        maxHeap = [-cnt for cnt in count.values()]
                heapq.heappush(maxHeap, q.popleft()[0])                heapq.heappush(maxHeap, q.popleft()[0])
        return time        return time
