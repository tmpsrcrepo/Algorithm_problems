# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

#using union find (compression find: ~ O(1) in average, union: ~O(1))

from union_find import *
        
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
    
    
    
        
