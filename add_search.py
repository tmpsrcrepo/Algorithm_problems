class trieNode:
    def __init__(self):
        self.leaf = False
        self.words = {}
        
class WordDictionary:
    def __init__(self):
        self.root = trieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self,word):
        root = self.root
        for w in word:
            if w not in root.words:
                root.words[w] = trieNode()
            root = root.words[w]
        root.leaf = True
            
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self,word):
        return self.search_re(0,self.root,word)
        
    def search_re(self, i, root, word):
        if i == len(word):
            return root.leaf
        w = word[i]
        if w == '.':
            for nex,nex_obj in root.words.items():
                if self.search_re(i+1,nex_obj,word):
                    return True
        elif w in root.words and self.search_re(i+1,root.words[w],word):
            return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
