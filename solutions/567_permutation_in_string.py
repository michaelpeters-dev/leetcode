# Problem: Permutation in String
# Number: 567
# Difficulty: Medium
# URL: https://leetcode.com/problems/permutation-in-string/
# Submission Status: Accepted
# Runtime: 13 ms
# Memory: 17.43 MB


        s1_counts = [0] * 26        s1_counts = [0] * 26
        s2_counts = [0] * 26        s2_counts = [0] * 26

        for i in range(n1):        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - 97] += 1            s2_counts[ord(s2[i]) - 97] += 1
                
        if s1_counts == s2_counts:        if s1_counts == s2_counts:
            return True            return True
                
        for i in range(n1, n2):        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - 97] += 1            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:            if s1_counts == s2_counts:
                return True                return True
        return False        return False
