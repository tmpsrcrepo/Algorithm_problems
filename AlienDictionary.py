#topological sort
class AlienDictionary(object):
    def topologicalSort(self, edges, degrees,count):
        #BFS
        out = ''
        queue = collections.deque([k for k,v in degrees.items() if v==0])
        #print queue
        while queue:
            q = queue.popleft()
            out+=q
            for e in edges[q]:
                count-=1
                degrees[e]-=1
                if degrees[e]==0:
                    queue.append(e)
            
        #print count,out
        if count==0:
            return out
        return ''
    
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        lim = len(words)
        edges = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        numEdges = 0
        
        pre = ''
        
        for cur in words:
            for c in cur:
                if c not in degrees:
                    degrees[c] = 0
            
            
            for j in xrange(min(len(pre),len(cur))):
                c1 = pre[j]
                c2 = cur[j]
                if c2 not in degrees:
                    degrees[c2]=0    
                #important: if finds the first different pair, add the edge, and break
                if c1!=c2:
                    numEdges+=1
                    edges[c1].append(c2)
                    degrees[c2]+=1
                    lim1=j+1
                    break
            pre = cur
                    
        #print degrees
        return self.topologicalSort(edges,degrees,numEdges)
        
