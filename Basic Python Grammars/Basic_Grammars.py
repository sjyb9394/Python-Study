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
- Function is defiend using 'def' keyword:
  def add(x,y):
    return x+y
- A function does not have to return or get parameters. (void)
- Python use pass by assignment.
  1) The parameter passed in is actually a reference to an object. (but the reference is passed by value)
  2) If passing mutable object (list, dictionary..etc), it is passed by reference
  3) If passing immutable object (Integer, string, tuple...etc), it is passed by value
- If changing variable outside the function, use 'global' keyword.
  ex) a = 0
      def func():
         global a
         a+= 1
      for i in range(10):
         func()
      print(a) => 10
 - Lambda : Small anonymous function
    - Can take any number of arguments, but can only have one expression.
    - syntax: lambda arguments : expression
    ex) print( (lambda a, b: a + b) (3,7)) => 10

11. Class
- Python is object oriented programming language. Almost everythin in python is an object, with its properties and methods.
- A class is like an object constructor, or a "blueprint" for creating objects.
- To create a class, use keyword 'class:'
  ex) class Person:
        age = 5
        name = "Sam"
- To create an object:
  ex) P1 = Person()
      print(P1.age) => 5
- Constructor = __init__() function.
  ex) class Person:
          def __init__(self, name, age):
            self.name = name
            self.age = age
      P1 = Person("sam", 5)
- Self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class.
- Inheritance: Allows to define a class that inherits all the methods and properties from another class.
  a) Parent class: the class being inherited from (base class)
  b) Child class: the class that inherits from another class (derived class)
  For more information: [https://www.w3schools.com/python/python_inheritance.asp]

10. I/O
- Use input() to get data from keyboard. (input() returns string type)
- input().split() will split the input ans save in to variables.
  ex) a,b = input().split('-') => Input: 1-2 => a = 1 b = 2
- In order to change the data type use map().
  ex) map(int, input().split()) => will split the input and change to integer type.
- If there are too many input variables, instead of input(), use sys.stdin.readline()
  - imposrt sys
    data = sys.stdin.readline().rstrip()
    

 
 


  
