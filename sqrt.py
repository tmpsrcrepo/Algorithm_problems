
def mySqrt(x):
    start = 0
    end = x/2+1 #skip half of elements
    while start<=end: 
        mid = (start+end)/2
        cur = mid ** 2
        if cur == x:
            return mid
        elif cur < x:
            start = mid+1
        else:
            end = mid -1
        return mid
