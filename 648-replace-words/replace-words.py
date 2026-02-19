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
    
    def prefix(self, word):
        curr = self.root
        pre = ""
        for c in word:
            if c not in curr.children:
                return word
            curr = curr.children[c]
            pre += c
            if curr.endofword:
                return pre
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)
        
        sentences = sentence.split()
        ans = []

        for s in sentences:
            ans.append(trie.prefix(s))
        
        return " ".join(ans)
