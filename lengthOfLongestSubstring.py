#use DP + Hashmap: update the max length when a duplicate is found
def lengthOfLongestSubstring(s):
    dict_freq = {}
    max_count = 0
    tmp = 0
    last = 0
    for i in range(len(s)):
        st = s[i]
        if dict_freq.__contains__(st):
            #update the max_length when encounters a duplicate
            max_count = max(tmp,max_count)
            
            tmp_index = dict_freq.get(st)
            dict_freq[st]=i
            if tmp_index < last:
                tmp+=1
            else:
                last = tmp_index
                tmp = i-last   
            
        else:
            dict_freq[st]=i
            tmp +=1
           
    return max(max_count,tmp)
