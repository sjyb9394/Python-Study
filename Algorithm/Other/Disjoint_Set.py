"""
Disjoint Set
- Union Find data structure
- A data structure that stores a collection of disjoint (non-overlapping) sets.
- Using Tree:
  1) Using union operation, find root node for A and B.
  2) Repeat #1 until all of the union operationg is finished.
  
  ex) Say we have 1,2,3,4,5,6 nodes
  - Initially the table looks as follow:
  Node number 1 2 3 4  5  6
  Parent      1 2 3 4  5  6
  
  - Union 1 4
  Node number 1 2 3 4  5  6
  Parent      1 2 3 1  5  6
  
  - Union 2 3
  Node number 1 2 3 4  5  6
  Parent      1 2 2 1  5  6
  
  - Union 2 4
  Node number 1 2 3 4  5  6
  Parent      1 1 2 1  5  6
  
  - Union 5 6
  Node number 1 2 3 4  5  6
  Parent      1 1 2 1  5  5
  
  Result => {1,2,3,4} , {5,6}
"""

# Code
def find_parent(parent, x):
  if parent[x] != x:
    parent[x]  = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)
