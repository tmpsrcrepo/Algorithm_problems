
class unionFind:
    def __init__(self,parents):
        self.parents = parents
    '''compression find: improve the find cost -> improve union cost
    '''
        
    def find(self,x):
        #first find its root
        fa = parent = self.parents[x]
        while self.parents[parent] != parent:
            parent = self.parents[parent]
        
        #update predecessor of all the children of the root to the root=parent
        tmp = 0
        while self.parents[fa]!= fa:
            tmp = self.parents[fa]
            self.parents[fa] = parent
            fa = tmp
        return parent
        
    
    def union(self,p,q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent != q_parent:
            self.parents[p_parent] = q_parent
