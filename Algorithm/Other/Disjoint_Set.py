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
