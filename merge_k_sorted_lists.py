class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    #merge sort
    def merge(self,list1, list2):
        dummy = pt = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                pt.next = list1
                list1 = list1.next
            else:
                pt.next = list2
                list2 = list2.next
            pt = pt.next
        if not list2:
            pt.next = list1
        else:
            pt.next = list2
        return dummy.next
        
    def mergeKLists(self,lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)/2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left,right)

    
    
    import heapq
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return lists
        
        dummy = cur = ListNode(0)
        heap = [(node.val,node) for node in lists if node]
        heapq.heapify(heap)
        root = heap
        
        while len(heap)>0:#nk
            #log(k)
            tmp = heapq.heappop(heap)[1]
            #print tmp.val
            cur.next = tmp
            nxt = tmp.next
            if nxt:
                heapq.heappush(heap,(nxt.val,nxt))
            cur = tmp
        
        #nk(log(k))
        return dummy.next
