# Problem: Edit Distance
# Number: 72
# Difficulty: Medium
# URL: https://leetcode.com/problems/edit-distance/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        cache = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]        cache = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:                if word1[i] == word2[j]:
        return cache[0][0]        return cache[0][0]
                    cache[i][j] = cache[i + 1][j + 1]                    cache[i][j] = cache[i + 1][j + 1]
                else:                else:
                    cache[i][j] = 1 + min(cache[i][j + 1], cache[i + 1][j], cache[i + 1][j + 1])                    cache[i][j] = 1 + min(cache[i][j + 1], cache[i + 1][j], cache[i + 1][j + 1])
