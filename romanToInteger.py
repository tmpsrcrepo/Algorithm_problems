#using dictionary to look up is much faster
def romanToInt(s):
    conversion = {'I':1, 'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
    prev = conversion.get(s[0])
    output = prev
    if len(s)==1:
        return prev
    else:
        for i in s[1:]:

            cur = conversion.get(i)
            print 'previous',prev
            print 'current',cur
            if prev < cur:
                output -= prev
                output+=(cur - prev)
            else:
                output = output+ cur
            prev = cur
            print 'output',output
        return output
        
