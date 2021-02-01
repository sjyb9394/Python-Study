# Permutation
# - an arrangement of its members into a sequence or linear order, or if the set is already ordered, a rearrangement of its elements. (Order matters)
# nPr = n!/(n-r)!

import itertools
data = [1,2]
for x in itertools.permutation(data,2):
  print(list(x))
  
# Combination
# - Same concept as permutation but order doesn't matter
# nCr = n!/(r!*(n-r)!)

import itertools
data = [1,2,3]
for x in itertools.combinations(data,2):
  print(list(x), end = ' ')
