Dynamic Programming
- Dynamic Programming(DP) is an algorithmic technique for solving an optimazation problem by breaking it down into simpler subproblems and utilizaing the fact that
the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

Recurrence relation
- A recurrence relation is an equation that defines a sequence based on a rule that gives the next term as a function of the previous terms.
 ex) Fibonacci = f(x) = f(x-1) + f(x-2)
 - When we don't use dynamic programming -> Fibonacci's running time is O(2^n)
                                         -> For f(100) => 1,000,000,000,000,000,000,000,000,000,000 operations.
 
 Constraint
 - We can not use dynamic programming all the time.
 - We can use when:
  1) We can split the problems into sub-problems.
  2) The results from the subproblems is unchanged from the bigger problem.
  
  Memoization (Top Down)(Recursive)
  - Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached
  result when the same inputs occur again.
  
  ====Fibonacci using memoization====
  d = [0] * 100
  
  def fibo(x):
    if x==1 or x==2: return 1
    if d[x] != 0: return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
 ====================================
 => Simply using a data structure such as array, or list, store all the results and if there is a result for certain input already in the array, instead of computing again, just return the value.
 
 Bottom-up (Loop)
 ====================================
 d = [0] * 100
 
 d[1] = 1
 d[2] = 1
 n = 99
 
 for i in range(3, n+1):
  d[i] = d[i-1]+d[i-2]
 
print(d[n])
=====================================
 
 
