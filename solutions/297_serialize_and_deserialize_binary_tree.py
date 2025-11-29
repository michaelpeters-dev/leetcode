# Problem: Serialize and Deserialize Binary Tree
# Number: 297
# Difficulty: Hard
# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Submission Status: Accepted
# Runtime: N/A
# Memory: N/A

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root, res):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            dfs(root.left, res)
            dfs(root.right, res)
        dfs(root, res)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
