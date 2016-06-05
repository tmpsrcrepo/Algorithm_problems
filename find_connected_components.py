# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

#using union find (compression find: ~ O(1) in average, union: ~O(1))

class unionFind:
    def __init__(self,parents):
        self.parents = parents
    '''compression find: improve the find cost -> improve union cost
    '''
    def find(self,x):
        while x != self.parents[x]:
            #update its parent to its grandparents
            x = self.parents[x] = self.parents[self.parents[x]]
            #update x
        return x
        
    def find1(self,x):
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
        
class connected_components:
    def get_results(self,uf):
        res = []
        graph = collections.defaultdict(list)
        for i in sorted(uf.parents):
            parent = uf.find(i)
            graph[parent].append(i)
        
        for g in graph.values():
            res.append(sorted(g))
        return (res)
            
            
        
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        #initialization
        parents = {}
        
        for node in nodes:
            node_label = node.label
            parents[node_label] = node_label
            for n in node.neighbors:
                n_label = n.label
                parents[n_label] = n_label
        
        uf = unionFind(parents)
        
        for node in nodes:
            for n in node.neighbors:
                uf.union(node.label,n.label)
        
        return self.get_results(uf)
    
    
    
        
