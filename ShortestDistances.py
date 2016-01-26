class ShortestDistances(object):
    def BFS(self,w,h,b,grid,dist,count):
        visited  = [[0 for i in xrange(w)] for j in xrange(h)]
        queue = collections.deque([b])
        min_ = float('Inf')
        while queue:
            b = queue.popleft()
            x = b[0]
            y = b[1]        
            d = b[2] #important: memorize its level order (1: d=0, else d=d+level order
            
            d+=1
            for i in [x-1,x+1]:
                #if it's an unvisted empty space, find distance
                if i>=0 and i<h and visited[i][y]==0 and grid[i][y]==count:
                    dist[i][y] += d
                    min_ = min(dist[i][y],min_)
                    queue.append((i,y,d))
                    visited[i][y]=1
                    grid[i][y]-=1
            for j in [y-1,y+1]:
                #if it's an unvisted empty space, find distance
                if j>=0 and j<w and visited[x][j]==0 and grid[x][j]==count:
                    dist[x][j] += d
                    min_ = min(dist[x][j],min_)
                    queue.append((x,j,d))
                    visited[x][j]=1
                    grid[x][j]-=1  
        return min_
    
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        h = len(grid)
        if h==0:
            return 0
        w = len(grid[0])
        min_ = float('Inf')
        si = 0
        sj = 0
        
        dist = [[0 for i in xrange(w)] for j in xrange(h)]
        #use the BFS (find the shortest distance)
        #if find a position which can be reached by all the buildings
        #shortest distance reached by every building: sum of BFS distance from each building
        
        #O(k*m*n), k = number of buildings
        
        #find the 1's
        numBuildings = 0

        for i in xrange(h):
            for j in xrange(w):
                if grid[i][j]==1:
                    
                    #each building: calculate distances from each empty cell to the building (BFS)
                    b = (i,j,0)
                    min_ = self.BFS(w,h,b,grid,dist,numBuildings)
                    numBuildings-=1
        
        #for b in buildings:
        #print dist
    
        if min_ == float('Inf'):
            return -1
        return min_
