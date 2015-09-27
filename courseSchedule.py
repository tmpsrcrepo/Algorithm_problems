# given a list of (prereq, course) pairs and total number of courses
# find out if it's possible to finish all the courses

# solution: turn these pairs into a graph structure (DAG)
# and find out if it's possible to visit every edge (= pair)
# by topological sort. If there's a cycle -> some edges left and it's impossible to finish each course

class finishClass(object):
    def BFStopological(self,numCourse,prerequisites):
        #create graph
        count = len(prerequisites)
        graph = {i:[] for i in range(0,numCourse)}
        incoming = {i:0 for i in range(0,numCourse)}
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            incoming[pair[0]]+=1
        S = collections.deque([node for node,e in incoming.items() if e==0])
        while S:
            tmpNode = S.popleft()
            print tmpNode
            for m in graph[tmpNode]:
                count-=1
                incoming[m]-=1
                if incoming[m] == 0:
                    S.append(m)
        return count==0
