def reverseWords(s):
    if s=="":
        return s;
    else:
        lim = len(s)
        res = ""
        tmp=""
        for i in range(0,lim):
            w = s[lim-1-i]
            
            if w==" ":
                if tmp!="":
                    res = res+(tmp)
                    tmp =""
            else:
                tmp = w+tmp
        return (res+tmp).strip()
            
