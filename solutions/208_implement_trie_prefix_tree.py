# Problem: Implement Trie (Prefix Tree)
# Number: 208
# Difficulty: Medium
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = False

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = self.TrieNode()
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
