# Problem: Top K Frequent Elements
# Number: 347
# Difficulty: Medium
# URL: https://leetcode.com/problems/top-k-frequent-elements/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 21.00 MB

class·‌Solution:class·‌Solution:
·‌·‌·‌·‌def·‌topKFrequent(self,·‌nums:·‌List[int],·‌k:·‌int)·‌->·‌List[int]:·‌·‌·‌·‌def·‌topKFrequent(self,·‌nums:·‌List[int],·‌k:·‌int)·‌->·‌List[int]:
·‌·‌·‌·‌·‌·‌·‌·‌count·‌=·‌{}·‌·‌·‌·‌·‌·‌·‌·‌count·‌=·‌{}
·‌·‌·‌·‌·‌·‌·‌·‌freq·‌=·‌[[]·‌for·‌i·‌in·‌range(len(nums)·‌+·‌1)]·‌·‌·‌·‌·‌·‌·‌·‌freq·‌=·‌[[]·‌for·‌i·‌in·‌range(len(nums)·‌+·‌1)]

·‌·‌·‌·‌·‌·‌·‌·‌for·‌n·‌in·‌nums:·‌·‌·‌·‌·‌·‌·‌·‌for·‌n·‌in·‌nums:
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌count[n]·‌=·‌1·‌+·‌count.get(n,·‌0)·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌count[n]·‌=·‌1·‌+·‌count.get(n,·‌0)
·‌·‌·‌·‌·‌·‌·‌·‌for·‌n,·‌c·‌in·‌count.items():·‌·‌·‌·‌·‌·‌·‌·‌for·‌n,·‌c·‌in·‌count.items():
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌freq[c].append(n)·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌freq[c].append(n)

·‌·‌·‌·‌·‌·‌·‌·‌res·‌=·‌[]·‌·‌·‌·‌·‌·‌·‌·‌res·‌=·‌[]
·‌·‌·‌·‌·‌·‌·‌·‌for·‌i·‌in·‌range(len(freq)·‌-·‌1,·‌0,·‌-1):·‌·‌·‌·‌·‌·‌·‌·‌for·‌i·‌in·‌range(len(freq)·‌-·‌1,·‌0,·‌-1):
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌for·‌n·‌in·‌freq[i]:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌for·‌n·‌in·‌freq[i]:
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌res.append(n)·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌res.append(n)
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌len(res)==k:·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌if·‌len(res)==k:
·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌return·‌res·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌·‌return·‌res
