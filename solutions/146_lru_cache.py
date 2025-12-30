# Problem: LRU Cache
# Number: 146
# Difficulty: Medium
# URL: https://leetcode.com/problems/lru-cache/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: N/A

            self.remove(self.cache[key])            self.remove(self.cache[key])
            self.insert(self.cache[key])            self.insert(self.cache[key])
        if key in self.cache:        if key in self.cache:
    def get(self, key: int) -> int:    def get(self, key: int) -> int:
        


        prev, nxt = self.right.prev, self.right        prev, nxt = self.right.prev, self.right
    def insert(self, node):    def insert(self, node):
    # instert node at right    # instert node at right
        
    def remove(self, node):    def remove(self, node):
    # remove node from list    # remove node from list

        prev, nxt = node.prev, node.next        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev        prev.next, nxt.prev = nxt, prev
        prev.next = nxt.prev = node        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev        node.next, node.prev = nxt, prev
