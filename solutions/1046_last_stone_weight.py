# Problem: Last Stone Weight
# Number: 1046
# Difficulty: Easy
# URL: https://leetcode.com/problems/last-stone-weight/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                        
            y = arr[-1]            y = arr[-1]
            x = arr[-2]            x = arr[-2]

            if x==y:            if x==y:
                arr.remove(x)                arr.remove(x)
                arr.remove(y)                arr.remove(y)
            else:            else:
                return arr[0]                return arr[0]
                arr.remove(x)                arr.remove(x)
                arr[-1] = y - x                arr[-1] = y - x
            return dfs(arr)            return dfs(arr)
        return dfs(stones)        return dfs(stones)
