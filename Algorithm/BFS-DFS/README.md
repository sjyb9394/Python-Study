Stack = LIFO (Last in First out)
  - Use append(), pop() methods from list
Queue = FIFO (First in First out)
  - Use deque from collections library
  - append() and popleft()
  - Deque can be use for both stack and queue. 

How to show graph in programming:
1) Adjacency Matrix: Square matrix used to represent a finite graph.
2) Adjacency List: Collection of unordered lists used to represent a finite graph.
  
Example for both : https://algorithmtutor.com/images/graph_representation_directed.png

DFS - Depth-First Search
 - Use stack for implementing DFS
 
 Step:  1) Insert start node to stack and mark visited.
        2) If there is unvisited adjacency node for the node from top of the stack, insert that node into stack. 
        3) If all adjacency nodes are visited, take out the top node from the stack.
        4) Repeat 2-3 until all nodes are maked visited.
        
 
