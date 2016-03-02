def findBomb(A):
    
    last = -1
    count = 0

    for i,a in enumerate(A[:-1]):
        if a==A[i+1]:
            if a==1+last:
                count+=1
                if count == 3:
                    return True
            elif a>1+last:
                count = 1
            last = a

    return False

print findBomb([1,2,2,3,3,4,5,5])
print findBomb([1,1,2,2,3,3,4,4,5])
print findBomb([1,1,2,2,4,4])
print findBomb([1,2,2,3,3,3,3,3,3,3,3,3,3,4,4,5])
print findBomb([1,1,2,2,2,2,2,2,2,3,3])
