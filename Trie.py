class TrieNode(object):
    def __init__(self):
        self.leaf = False
        self.child = [None]*26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root
        for char in word:
            tmp = ord(char)-ord('a')
            if not root.child[tmp]:
                root.child[tmp] = TrieNode()
            root = root.child[tmp]
        root.leaf = True
        

    def search(self, word):
        root = self.root
        for char in word:

            tmp = ord(char)-ord('a')
            root = root.child[tmp]
            if not root:
                return False
        return root.leaf

    def startsWith(self, prefix):
        root = self.root
        for char in prefix:

            tmp = ord(char)-ord('a')
            root = root.child[tmp]
            if not root:
                return False
        return True

# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
