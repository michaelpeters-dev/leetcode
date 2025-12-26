# Problem: Word Ladder
# Number: 127
# Difficulty: Hard
# URL: https://leetcode.com/problems/word-ladder/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

        visit = set([beginWord])        visit = set([beginWord])
        q = deque([beginWord])        q = deque([beginWord])
        res = 1        res = 1

        while q:        while q:
            for i in range(len(q)):            for i in range(len(q)):
                word = q.popleft()                word = q.popleft()
                for j in range(len(word)):                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]                    pattern = word[:j] + "*" + word[j + 1:]
                if word==endWord:                if word==endWord:
                    return res                    return res
                    for neiWord in nei[pattern]:                    for neiWord in nei[pattern]:
                            q.append(neiWord)                            q.append(neiWord)
                        if neiWord not in visit:                        if neiWord not in visit:
                            visit.add(neiWord)                            visit.add(neiWord)
        return 0        return 0
            res += 1            res += 1

