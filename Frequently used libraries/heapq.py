# heapq : Provides an implementation of the heap queue algorithm, also known as the priority queue algorithm
# - Heaps are binary trees for which every parent node has a value less than or equal to any of its children.
# - Use Min Heap as default.
# 1. heappush() - Insert an element, maintaining the heap variant. O(log n)
# 2. heappop() - Pop and return the smallest element               O(log n)

#heapsort example
import heapq
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h,value)
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1,2,4,7,9,2,4,6,8,0])
print(result)
=>[0, 1, 2, 2, 4, 4, 6, 7, 8, 9]

#heapq reverse sort example (Simply change the sign when inserting and popping)
import heapq
def heapsort(iterable):
  h = []
  result = []
  for value in iterable:
    heapq.heappush(h,-value)
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1,2,4,7,9,2,4,6,8,0])
print(result)
=>[9, 8, 7, 6, 4, 4, 2, 2, 1, 0]
