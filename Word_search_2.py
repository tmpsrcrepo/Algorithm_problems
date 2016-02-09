class TrieNode(object):
    def __init__(self):
        self.childs = {}
        self.leaf = False
class Solution(object):
    
    #build trie out of words
    def buildTree(self,root,word):
        for w in word:
            if w not in root.childs:
                root.childs[w] = TrieNode()
            root = root.childs[w]
        root.leaf = True
    
    def backtrack(self,board,i,j,root,tmp,res):
        #print tmp,root.childs
        if root.leaf == True:
            res.append(tmp)
        w= board[i][j]
        board[i][j]='.'
        for c,v in root.childs.items():
            if i>0 and board[i-1][j]==c:
                self.backtrack(board,i-1,j,v,tmp+c,res)
            if j>0 and board[i][j-1]==c:
                self.backtrack(board,i,j-1,v,tmp+c,res)
            if i+1 < len(board) and board[i+1][j]==c:
                self.backtrack(board,i+1,j,v,tmp+c,res)
            if j+1 <len(board[0]) and board[i][j+1]==c:
                self.backtrack(board,i,j+1,v,tmp+c,res)
        board[i][j] = w
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #build trie tree:
        root = TrieNode()
        for word in words:
            cur = root
            self.buildTree(cur,word)
        
        #search prefix:
        res = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                w = board[i][j]
                if w in root.childs:
                    #print root.childs[w].childs
                    #print w
                    self.backtrack(board,i,j,root.childs[w],w,res)
            
        return list(set(res))
