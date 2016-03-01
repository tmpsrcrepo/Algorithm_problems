#https://www.careercup.com/question?id=5725353829990400
import collections

def direction(matrix,m,n,i,j,queue,counter):
    for a,b in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]:
        if a>=0 and b>=0 and a<m and b<n:
            if matrix[a][b]  == 1:
                matrix[a][b] = counter
                queue.append((a,b))
            if matrix[a][b] == 'E':
                break



def bfs(matrix):
    if not matrix:
        return

    queue = collections.deque()
    m = len(matrix)
    n = len(matrix[0])

    #first, find the start point
    for i in xrange(m):
        for j in xrange(n):
            if matrix[i][j]=='S':
                matrix[i][j] = 0
                queue.append((i,j))
    v = 0
    #BFS, increment counter each time when we find 1's. Terminate when we find 'E' point
    while queue:
        print queue
        i,j = queue.popleft()
        #matrix[i][j] = 'X' #mark visited
        v = matrix[i][j]
        direction(matrix,m,n,i,j,queue,v+1)
    return v-1




matrix = [[1,1,1,1,1],['S',1,'X',1,1],[1,1,1,1,1],['X',1,1,'E',1],[1,1,1,1,'X']]
print bfs(matrix)
