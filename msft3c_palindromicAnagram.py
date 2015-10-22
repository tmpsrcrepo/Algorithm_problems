import collections
import numpy as np
import math


"""
Microsoft college coding competition question

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. An anagram is the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all of the original letters exactly once.

This problem is a combination of both. You will be given a string and your program needs to check whether or not any of its anagrams contain a palindrome. If none of the anagrams is a palindrome, then you need to find the minimum number of characters to eliminate from the string in order for at least one of its anagrams to be a palindrome. In addition, your program needs to figure out the number of anagrams that are palindromes.

Consider this example: You are given the string "aabd". None of the anagrams of this string are palindrome. If you remove the letter "d", however, then "aba" is an anagram of the string that is a palindrome; if you remove the letter "b", then "ada" is an anagram that is a palindrome. In either case, there is only one anagram that is a palindrome.
"""

class Solution(object):
    def find(self,str_):
        uniq = len(collections.Counter(str_).keys())
        freq = collections.Counter(str_).values()
        divisible = [i%2 for i in freq]
        
        change = np.sum(divisible)-1
        
        total = np.sum(freq)
        fac = 1
        if change > 0:
            uniq-=change
            total -=change
        for f in freq:
            if f%2==1:
                f-=1
            f = f/2
            if f>1:
                fac=(fac*math.factorial(f))

        
        res =math.factorial(total/2)/(fac)
        #res = max(1,res/2)
        return max(0,change),res


s = Solution()
#print s.find('nnnnjjjnnnjjsss')
for line in open('PracticeInput_Palindromic.txt','r'):
    print s.find(line.rstrip())
