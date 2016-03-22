class word_break_solution(object):
    def dfs(self,remainStr,wordDict,cache):
        if remainStr:
            if remainStr in cache:
                return cache[remainStr]
            ret = []
            for i in xrange(len(remainStr)):
                if remainStr[:i+1] in wordDict:
                    for r in self.dfs(remainStr[i+1:],wordDict,cache):
                        ret.append((remainStr[:i+1]+' '+r).strip())
            cache[remainStr]=ret
            return ret
        return ['']
        
    def wordBreak(self,s,wordDict):
        return self.dfs(s,wordDict,{})
