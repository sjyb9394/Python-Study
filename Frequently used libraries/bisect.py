# bisect : Provides support for maintaining a list in sorted order without having to sort the list after each insertion (Binary search)
# -Similar to upper_bound and lower_bound from c++
# a) bisect_left(a,x): Maintaining a list in sorted order, find the index for the insertion point for x in a to most left side.
# b) bisect_right(a,x): Maintaining a list in sorted order, find the index for the insertion point for x in a to most right side.

#ex 1
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

=> 2
   4
   
#ex 2 (Count by range)
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a,left_value)
  return right_index-left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a,4,4))
print(count_by_range(a,-1,3))

=> 2
   6
