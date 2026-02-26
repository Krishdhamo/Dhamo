# priority queue 
# remove elements based on priority instead of order

# highest priority removed first 
# not normal fifo
# smaller number = highest priority

# task -1
# task -2
# task -3

# real time eg
# hospital emergency room
# cpu task scheduling
# printer task priority 
# network packet routing

# normal queue vs priority queue
# Normal Queue (FIFO - First In First Out)

# heap
# smallest number = highest priority
# automatic sorting
# uses heap module 

# pseudocode
# insert 
# create empty priority queue
# insert elements with priority
# heap arranges automatically

# remove 
# remove smallest priority element 

# import heapq

# pq = []

# heapq.heappush(pq,2,"medium task")
# heapq.heappush(pq,1,"high task")
# heapq.heappush(pq,3,"low task")
# while pq:
#     priority,task = heapq.heappop(pq)
#     print(priority,task)
# print("priority Queue ",pq)

# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))
# print("removed",heapq.heappop(pq))

# def deleteDuplicates(self, head):
#     """
#     :type head: Optional[ListNode]
#     :rtype: Optional[ListNode]
#     """
#     if not head:
#         return None
#     current = head
#     while current and current.next:
#         if current.val == current.next.val:
#             current.next = current.next.next
#         else:
#             current = current.next
#     return head

