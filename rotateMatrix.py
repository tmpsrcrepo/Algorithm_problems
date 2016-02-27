def rotate90degrees(self, matrix):
    # nxn matrix
    t = 0
    n = len(matrix)
    
    
    
    for i in xrange(n):
        for j in xrange(i,n-i-1):
            #propagate the change matrix[x][y] to matrix[y][n-x-1] and then repeate three times
            t = matrix[i][j]
            matrix[j][n-i-1],t = t,matrix[j][n-i-1]
            t,matrix[n-i-1][n-j-1] =matrix[n-i-1][n-j-1],t
            t,matrix[n-j-1][i]=matrix[n-j-1][i],t
            t,matrix[i][j] = matrix[i][j],t
            
