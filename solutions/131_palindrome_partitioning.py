# Problem: Palindrome Partitioning
# Number: 131
# Difficulty: Medium
# URL: https://leetcode.com/problems/palindrome-partitioning/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

                    dfs(j + 1)                    dfs(j + 1)
                    part.pop()                    part.pop()
                        
        dfs(0)        dfs(0)
        return res        return res
                    part.append(s[i:j+1])                    part.append(s[i:j+1])

    def isPali(self, s, l, r):    def isPali(self, s, l, r):
        while l<=r:        while l<=r:
            if s[l]!=s[r]:            if s[l]!=s[r]:
                return False                return False
            l += 1            l += 1
            r -= 1            r -= 1
        return True        return True
