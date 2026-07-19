# Problem: Implement Trie (Prefix Tree)
# Number: 208
# Difficulty: Medium
# URL: https://leetcode.com/problems/implement-trie-prefix-tree/
# Submission Status: Accepted
# Runtime: 0 ms
# Memory: 0.00 MB

    }    }
        
    bool startsWith(string prefix) {    bool startsWith(string prefix) {
        Trie* curr = this;        Trie* curr = this;

        for (char& letter: prefix) {        for (char& letter: prefix) {
            if (!curr->children.count(letter)) {            if (!curr->children.count(letter)) {
                return false;                return false;
            }            }

            curr = curr->children[letter];            curr = curr->children[letter];
        }        }

        return curr->isEnd;        return curr->isEnd;
            }            }
            curr = curr->children[letter];            curr = curr->children[letter];
        }        }

    }    }
};};

/**/**
 * Your Trie object will be instantiated and called as such: * Your Trie object will be instantiated and called as such:
        return true;        return true;
