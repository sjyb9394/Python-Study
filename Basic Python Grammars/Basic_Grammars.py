1. Data (Arithmetic)
- Integers: Positive, Negative, 0
- Real Numbers: Positive, Negative decimal numbers => Use floating point
  - Can use e or E for exponent 
  ex) a = 75e9 => 75000000000
      b = 3954e-3 => 3.954
  - Computer has limit to show the floating numbers because computer use binary numbers for all operations
    -> When adding 0.3 and 0.6, the result should be 0.9, however, there is no way to show 0.9 in binary, therefore the result will be 0.899999999999... 
        => Need to round up to show it correctly.
- Use +, -, *, /, //, ** for arithmetic operation.

2. List
- Initialize with [] and separate the datas with ,(comma).
- Similar to arrays in c++.
- Can be use negative number for indexing. a[-1] -> will check last element.
- Slicing = use colon(:) for slicing. ex) a[1 : 4] will check from index 1 to 3.
- List comprehension: A way to initialize the list by using for loop in one line.
  ex) array = [i for i in range(20) if i % 2 == 1] => list with odd numbers between 0~19
      array = [i*i for i in range(1,10)]           => list with (i*i) between 1~9
- 2d list initialization
  ex) n = 3 
      m = 4
       array = [[0] * m for _ in range(n)] => array[3][4] list
       [[0]*m]*n => wrong way to initialize. This will have 2d array, but this list will have same reference to all inner lists.
- Method: append O(1), sort, reverse, insert O(N), count, remove O(N)

  EX) Remove certain elements
      a = [1,2,3,4,5,5,5]
      remove = [3,5]
      result = [i for i in a if i not in remove] => [1,2,4]
      
3. String
- Use '' or "" for initialization.                        => a = '' or a = ""
- Use \ to print out ".                                   => print("\"Example\"")
- Use + or , to combine several strings.                  => print("Hello"+"World") or print("Hello","World")
- Use * (positive integer) to print out multiple times.   => print("asdf" * 3)
- Can use indexing or slicing just like a List.

4. Dictionary
- Similar to map in C++
- Used to stroe values in key:value pairs.
- Unordered, changeable and does not allow duplicates (key).
- Initialize with {}
- O(1) for search, and modify.
- Use in to search for an element. (List and Tuple can use in or not in)
- key() return only key elements and values() return only value elements.

5. Tuple
- Used to store multiple items in a single variables.
- Ordered and unchangeable.
- Written with (,,) => a = (1,2,3,4)

6. Set
- Used to store multiple items in a single variable.
- Unordered, unindexed, unchangeable and do not allow duplicate values.
- Use {} and , for initialization.
- Operations: 
   a) & : Intersection
   b) | : Union
   c) - : Difference
- add() : Use to add 1 element
- update([]) : Use to add multiple elements
- remove() : Use certain element

7. If else Condition Statement
- if, elif, and else.
- Comparison operations: ==, !=, <, <=, >, >=
- Logical operations: and, or, not
- Other operations: in, not in (for list, tuple, string, dictionary)
- One line syntax: (value if true) if (condition) else (value if false)
- One line syntax with for loop: 
  - When using if , for : => a = [i * 2 for i in range(5) if i % 2 == 0]
  - When using if, else, for : => a = [i if i % 2 == 0 else 1 for i in range(5)]

8. Loops
- while loop is similar to other programming languages:
    while condition:
       code
- for: Python use (for in) loop as default.
  for variable in data-type or for variable in range(integger)
- Can use break or continue.

9. Functions

11. Class

10. I/O


 
 


  
