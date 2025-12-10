class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for w in words:
            trie.addWord(w)

        n, m = len(board), len(board[0])
        res = set()
        vis = set()

        def dfs(i, j, node, word):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if (i, j) in vis:
                return
            c = board[i][j]
            if c not in node.children:
                return

            vis.add((i, j))
            node = node.children[c]
            word += c

            if node.endofword:
                res.add(word)

            dfs(i+1, j, node, word)
            dfs(i-1, j, node, word)
            dfs(i, j+1, node, word)
            dfs(i, j-1, node, word)

            vis.remove((i, j))

        for i in range(n):
            for j in range(m):
                dfs(i, j, trie.root, "")

        return list(res)
