#find the max number of points on the same line
#classic algorithm problem
class maxPoints(object):
    def calc_diff_pairs(self,ox,oy,index,points):
        v = 0
        same = 1
        vertical = 1
        diff_pairs=[]
        for p in points[index+1:]:
            if p.y==oy and p.x == ox:
                same+=1
            elif p.y==oy:
                vertical+=1
            else:
                diff_pairs.append((p.x-ox)/(1.0*(p.y-oy)))
        return diff_pairs,same,vertical
    
    def maxPoints(self, points):
        if not points:
            return 0
        maxCount = 1
        #sort the points based on x-coordinates - calculate gradients only w/ respect to 
        #points further than/equal to their x-coordinates
        
        #points = (sorted(points, key=lambda points:points.x))
        
        for i,p in enumerate(points):
            ox = p.x
            oy = p.y
            #print ox,oy
            table = collections.defaultdict(int)
            
            diff_pairs,same,vertical = self.calc_diff_pairs(ox,oy,i,points)
            for d in diff_pairs:
                table[d]+=1
                maxCount = max(maxCount,table[d]+same)
            maxCount = max(maxCount,vertical,same)
            #print table
                
        
        return maxCount
