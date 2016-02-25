class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leaf = False
        self.child = [None]*26

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for char in word:
            tmp = ord(char)-ord('a')
            if not root.child[tmp]:
                root.child[tmp] = TrieNode()
            root = root.child[tmp]
        root.leaf = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for char in word:

            tmp = ord(char)-ord('a')
            root = root.child[tmp]
            if not root:
                return False
        return root.leaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for char in prefix:

            tmp = ord(char)-ord('a')
            root = root.child[tmp]
            if not root:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
