# collections: provides specialized container datatypes (data structures)
# deque: List-like container with fast appends and pops on either end
#         - Can't use indexing or slicing.
#         - Can be used as stack or queue.
#    a) appendleft(x) - Add x to the left side 
#    b) append(x)     - Add x to the right side
#    c) popleft()     - Remove and return an element from left side
#    d) pop()         - Remove and return an element from right side
# Counter: dict-like class for creating a single view of multiple mappings

# Running time comparison :            List  deque
# Add to first index                   O(N)  O(1)
# Add to last index                    O(1)  O(1)
# Pops and return from first index     O(N)  O(1)
# Pops and return from last index      O(1)  O(1)

ex) Basic grammar practice
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

=>deque([1, 2, 3, 4, 5])
  [1, 2, 3, 4, 5]
  
# Counter example
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict[counter])

=>3
  1
  dict[Counter({'blue': 3, 'red': 2, 'green': 1})] # change type to dictionary
