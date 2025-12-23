# Problem: Interleaving String
# Number: 97
# Difficulty: Medium
# URL: https://leetcode.com/problems/interleaving-string/
# Submission Status: Accepted
# Runtime: 36 ms
# Memory: N/A

class·‌Solution:class·‌Solution:
·‌·‌·‌·‌def·‌isInterleave(self,·‌s1:·‌str,·‌s2:·‌str,·‌s3:·‌str)·‌->·‌bool:·‌·‌·‌·‌def·‌isInterleave(self,·‌s1:·‌str,·‌s2:·‌str,·‌s3:·‌str)·‌->·‌bool:
·‌·‌·‌·‌·‌·‌·‌·‌if·‌len(s1)·‌+·‌len(s2)·‌!=·‌len(s3):·‌·‌·‌·‌·‌·‌·‌·‌if·‌len(s1)·‌+·‌len(s2)·‌!=·‌len(s3):
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌return·‌False·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌return·‌False
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌
·‌·‌·‌·‌·‌·‌·‌·‌dp·‌=·‌[[False]·‌*·‌(len(s2)·‌+·‌1)·‌for·‌i·‌in·‌range(len(s1)·‌+·‌1)]·‌·‌·‌·‌·‌·‌·‌·‌dp·‌=·‌[[False]·‌*·‌(len(s2)·‌+·‌1)·‌for·‌i·‌in·‌range(len(s1)·‌+·‌1)]
·‌·‌·‌·‌·‌·‌·‌·‌dp[len(s1)][len(s2)]·‌=·‌True·‌·‌·‌·‌·‌·‌·‌·‌dp[len(s1)][len(s2)]·‌=·‌True

·‌·‌·‌·‌·‌·‌·‌·‌for·‌i·‌in·‌range(len(s1),·‌-1,·‌-1):·‌·‌·‌·‌·‌·‌·‌·‌for·‌i·‌in·‌range(len(s1),·‌-1,·‌-1):
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌for·‌j·‌in·‌range(len(s2),·‌-1,·‌-1):·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌for·‌j·‌in·‌range(len(s2),·‌-1,·‌-1):
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌i<len(s1)·‌and·‌s1[i]==s3[i·‌+·‌j]·‌and·‌dp[i·‌+·‌1][j]:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌i<len(s1)·‌and·‌s1[i]==s3[i·‌+·‌j]·‌and·‌dp[i·‌+·‌1][j]:
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌dp[i][j]·‌=·‌True·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌dp[i][j]·‌=·‌True
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌j<len(s2)·‌and·‌s2[j]==s3[i·‌+·‌j]·‌and·‌dp[i][j·‌+·‌1]:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌j<len(s2)·‌and·‌s2[j]==s3[i·‌+·‌j]·‌and·‌dp[i][j·‌+·‌1]:
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌dp[i][j]·‌=·‌True·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌dp[i][j]·‌=·‌True
·‌·‌·‌·‌·‌·‌·‌·‌return·‌dp[0][0]·‌·‌·‌·‌·‌·‌·‌·‌return·‌dp[0][0]
