<h3>Stack = LIFO (Last in First out) </h3>
- Use append(), pop() methods from list <br />

<h3>Queue = FIFO (First in First out)</h3>
- Use deque from collections library <br />
- append() and popleft() <br />
- Deque can be use for both stack and queue. <br />

<h4>How to show graph in programming:</h4>
 1. Adjacency Matrix: Square matrix used to represent a finite graph.<br />
 2. Adjacency List: Collection of unordered lists used to represent a finite graph.
  
Example for both : https://algorithmtutor.com/images/graph_representation_directed.png

<h3>DFS - Depth-First Search </h3>
 - Use stack for implementing DFS<br />
 
 Step:  
 1. Insert start node to stack and mark visited. <br />
 2. If there is unvisited adjacency node for the top node from the stack, insert that node into stack. <br />
 3. If all adjacency nodes are visited, take out the top node from the stack.<br />
 4. Repeat 2-3 until all nodes are maked visited.<br />
        
 
<h3>BFS - Breadth First Search</h3>
- Use queue for implementing BFS<br />

Step:
1. Insert start node to queue and mark visited. <br />
2. Pop the first node, and insert all unvisited adjacency nodes to the queue <br />
3. Repeat #2 until all nodes are marked visted.

