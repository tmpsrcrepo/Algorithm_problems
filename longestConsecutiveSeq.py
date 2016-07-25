#longest consecutive sequence
class unionFind:
    def __init__(self,parents,counts):
        self.parents = parents
        self.counts = counts
        
    def find(self,x):
        fa = parent = self.parents[x]
        while self.parents[parent] != parent:
            parent = self.parents[parent]
        return parent

    def union(self,p,q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent != q_parent:
            self.parents[p_parent] = q_parent
            self.counts[q_parent] += self.counts[p_parent]


class Solution(object):
    def longestConsecutive(self, nums):
        
        parents = {n:n for n in nums}
        counts = {n:1 for n in nums}
        uf = unionFind(parents,counts)
        
        for p in parents:
            if p-1 in parents:
                uf.union(p,p-1)
        
        return max(counts.values())
            
        
