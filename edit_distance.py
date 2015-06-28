def minDistance(word1,word2):
    n=len(word1)
    m=len(word2)
    if n==0 or m==0:
        return max(n,m)
    D = [[0 for y in range(0,m+1)] for x in range(0,n+1)]
    for x in range(1,n+1):
        D[x][0]=x
    for y in range(1,m+1):
        D[0][y]=y
    for x in range(1,n+1):
        for y in range(1,m+1):
            D[x][y] = min(D[x-1][y]+1,D[x][y-1]+1,D[x-1][y-1]+int(word1[x-1]!=word2[y-1]))
    #return D[len(word1)-1][len(word2)-1]
    return D[-1][-1]
    
    
#initialize the matrix only once
def minDistance1(word1, word2):
    #initialization
    if len(word1)==0 or len(word2)==0:
        return max(len(word1),len(word2))
    else:
        D = [[max(y,x) if y==0 or x ==0 else 0 for y in range(0,len(word2)+1)] for x in range(0,len(word1)+1)]        
        for x in range(1,len(word1)+1):
            for y in range(1,len(word2)+1):
                D[x][y] = min(D[x-1][y]+1,D[x][y-1]+1,D[x-1][y-1]+int(word1[x-1]!=word2[y-1]))
        #return D[len(word1)-1][len(word2)-1]
        return D[len(word1)][len(word2)]
