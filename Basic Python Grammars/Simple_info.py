Simple python information.
0. Interpreted language = A type of programming language for which there is an interpreter which runs over a virtual machine.
                        = The interpreter executes the code line by line and converts it into low level machine language.
                        Advantage = More flexible and often offer feature like dynamic typing and smaller program size.
                                  = The code itself is platform independent because interpreters execute the source program code themselves.
                        Disadvantage = Slower.
   Compiled Language = Are converted directly into machine code that the processor can execute. As a result, they tend to be faster and more
                       efficient than interpreted languages.
                      Advantage = Faster.
                      Disadvantage = more time needed to complete the entire compilation step before testing
                                   = platform dependence of the generated binary code
1. sep = '' (Separate each elements)
  print('hi','how are you', sep=',') => hi, how are you

2. end = ''
  print('hi',end='')
  print('hello')      => hi hello (in one line)

3. round( number, digit number)
  print(rount(math.pi), 2) => 3.16
  print(rount(math.pi), 4) => 3.1616

4. help(), dir() 
   - help() returns explanations of the scope
   - dir() returns name of the methods of the scope

5. Use \ for printing certain symbols. And line break for code. (difference from \n)
  print('I dont't Know') => error
  print('I dont\'t know')
  print("Say "I don't know"") => error
  print("Say \"I don\'t know\"")
  path = "C:\\name\\path_name...." or path = r'C:\name\path...' (r = raw)

6. For printing multiple lines without using multiple print function
    print("""           print("""\     
    line1               line1
    line2         =>    line2
    line2               line2\
    """)                """)  (No blank space)

7. String is immutable, so if you want to change certain element in index, you need to copy the original one with new element.
  word = 'python'
  word[0] = 'j' => error
  word = 'j' + word[1:] => jython
  word = word[:3] + 't' + word[4:] => jytton
  or just use replace() method

8. List     []
   [::]
   => [::2] => access to even index
   => [::-1] => access from reverse order 
   l = [1,2,3,4]
   l[1:3] = [] => [1,4]
   - You can use del for delete element of the list or list itself.
   - You can also use remove method.
   index() = return the index of the certain element from left to right.
   index(3,4) => return the index of certain element (in this case int 3) after index 4.
   
   i = [1,2,3,4,5]
   j = i       => Even though it seems like j copied elements from i, but actually, only the name is different, they are using same list object.
   j[0] = 100
   print(j,i) => [100,2,3,4,5] [100,2,3,4,5] 
   - You need to use copy() method for shallow copy.  (Construct a new compound object and inserts references into it to the objects found in the original. Immutable elements will not be shared but mutable elements will)
   - You need to use deepcoy() method for deep copy. (Create everything new, new variable, new list object, but just same elements. (will iterate everything from orginial to copy the elements))
   Key
   1. Simple copy = Same object
   2. Shallow copy = New compund object but same reference.
   3. Deep copy = New compund object and copy the elements recursively. (Distinct object from original)
        
9. Tuple      ()
   - Can use almost every same method as list except changing the elements. Tuple is immutable.
   - Usually used for read, not for write

10. Dictionary    {key:value}
   - Update() = add if not exist, over-write if exist
   - get() = Find the value with key.
   - pop() = get and delete
   - clear() = Delete all key-value elements
   - Copying works same as List. (Reference, shallow, deep)
   - setdefault(key,value) = if key not in d: d[key]=value
        or        (works same)
   - from collections import defaultdict
        d = defaultdict(int)
        
              
11. Set         {}
   - Use {} without key-value
   - Has no sequence or order, cannot use 'set[0]'
   - add(), remove(), clear()...etc
   - Operation = -, &, |, ^
        1. -: Difference.
        2. &: Intersection
        3. |: Union
        4. ^: Symmetric difference.
 
12. is, ==
   - == : compares the value          (1 == True) => True
        -> usually use for compare the values
   - is : compare the object itself.  (1 is True) => False
        -> usually use for if the object is None or not
        
13. while-else/ for-else
   - else statement will be execute only if while-loop has been executed for all condition or statement without break statement.
        
14. zip: using in for loop, when trying to iterate more than one data-structure.
        ex) for day,fruit, drink in zip(days,fruits,drinks)
                print(day,fruit,drink)

15. Use items() method for iterating dictionary data structure.
        - items() returns tuple type for each element in side the list type wrapped by dictioniary_type().
        
16. Don't use list for default argument. ex) def ex(l=[]) => works correctly, but list is created only once and if this function is called more than one more time, 
        the object will be point to the same list's reference as previous one.
    If you want to check if the list's argument is empty, use 'l=None, and if l is None: ....'

17. *args = tuple argument. If number of argument is more than one, then all arguments will be sent in one tuple-type element.
        or we can send the argument as tuple-type element at first place.
        ex) def some_function(word, *args):....
            t = ('hi', 'hello')
            some_function('bye', *t)

    **kargs = similar to *args, but receive the argument as dictionary-type.

18. Docstrings : function_name.__doc__
  - returns the comment inside the function
 
19. Function inside the function can be used only in that function.
20. closure: 
  - A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
  - Closure can avoid the use of global values and provides some form of data hiding. It can also privoide an object oriented solution to the problem.
  - A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, 
  even when the function is invoked outside their scope.
  ex)def circle_area_func(pi):
        def circle_area(radius):
            return pi * radius * radius
        return circle_area
     ca1 = circle_area_func(3.14)
     ca2 = circle_area_funct(3.1416)
     print(ca1(5))
     print(ca2(10))
      
21. Decorator: a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
  ex)
  def print_info(func):
    def wrapper(*args, **kwargs):
      print('start')
      result = func(*args,**kwargs)
      print('end')
      return result
    return wrapper
  
  @print_info            Same process         
  def add_num(a,b):         =>           def add_num(a,b)
      return a+b                            return a+b
  
  r = add_num(10,20)                    f = print_info(add_num)
  print(r)                              r = f(10,20)
                                        print(r)
  - When using more than 1 decorator, you can write more than one decorators above the functino name
  ex) @print_info
      @print_more
      -> Sequence matters. print_info starts first, then execute print_more and termiante, then print_info terminate.
    
22. Lambda = Anonymous function
  Syntax = lambda argument: expression
        ex) lambda a : a + 10

23. Generator: Instead of iterate whole data, we can run and stop the loop whenever we want.
    1,Generator-Function : A generator-function is defined like a normal function, 
                           but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
                           If the body of a def contains yield, the function automatically becomes a generator function.
      ex) def ex():
              yield 'good morning'
              yield 'good afternoon'
          for i in ex():
            print(i)
            
    2. Generator-Object : Generator functions return a generator object. Generator objects are used either by calling the 
                          next method on the generator object or using the generator object in a “for in” loop (as shown in the above program).
     ex) x = ex()
         print(x.__next__())

24. Initialization of list, dict, set, generator in one line
    t = (1,2,3,4,5)
    f = (6,7,8,9,10)
    
    l = [i for i in t]  #list
    d = {x:y for x, y in zip(t,f)}  #dictionary
    
    #set
    s = set() 
    s = {x for x in t}
    
    #generator
    def g():
      for i in range(10):
        yield i
    
    g = (i for i in range(10))
 
25. Global, Local element
  ex) animal = 'cat'
      def f():
        print(animal)                                
        animal = 'dog'  => error, the value animal is globally used before this line. 
        print(animal)   
     -> If you want to get access to the global element, need to use global keyword inside the function.
     -> Use globals() or locals() when check if variable, method, functions are initiallized globally or locally.

26. try, except, else, finally
    try = only if there is no error
    except = runs if there is error.
    else = only there is no error after all cases are passed.
    finally = always executes after all of above codes are handled.
    
    Make my own error
    ex) use raise to error occurrence
    calss UppercaseError(Exception):
      pass
    
    def check():
        words = ['APPLE']
        for word in words:
          if word.isupper():
            raise UppercaseError(word)    
 
27. input argument in command line
    ls - list of files in current directory
    pwd - path of current directory
    cd - move to directory
    How to use arguement from command line
    python file.name arg1 arg2 ..... 
    
    - use import sys
          sys.argv => get argument from command line in list type. sys.argv[0] will have file name.
        
28. Module and packages
    - When import module by '*', the package needs to have __init__.py and __all__ = [module_name] in side the init file. 
    - Use try, except for importerror.
        try: 
          from .....
        except ImportError: 
          from .....
          
    - setup.py
      = Use setuptools for test, build, export in python.
      
      from setuptools import find_packages, setup
      
      setup(name=
            version=
            description=
            long_description=
            url=
            author=
            author_email=
            license=
            packages=
            classifiers=
            zip_safe=)
      #https://packaging.python.org/tutorials/packaging-projects/#setup-args
      or
      
      from distutils.core import setup
      
      setup(
           name=
           version=
           packages=
           url=
           license=
           author=
           author_email=
           description=
      )
      
     
      - Then use install, build, test from Command line.
      - python setup.py sdist for deploy file.
      
29. python standard library = https://docs.python.org/3.6/library/index.html      
30. import pretty way
    1. import standard library most above
    2. with one blank space import third-party library
    3. with one blank space my-own library
    4. with one blank space local-python library
    5. All alphabetical order.
   - use __file__ to find the path of the file.
   - sys.path = returns the path where the libraries are installed.
    
31. Override = Rewrite the method from parent class method
    Overload = Same method name but different parameter.
    super()= Returns a temporary object that allows reference to a parent class.
            - Avoid the usage of the super class explicitly.
            - Enable multiple inheritances.
    property = We can modify our class and implement the value constraint without any chnage required to the client code.
              - Use one _ to create property
              - Use two __ to create property but not accessible from outside of the class.
                      - If re-initializing as a struct, it will over-write.
              - @property = get the value
              - @value.setter = set the value
              - @value.deleter = deleting the value
 
32. Duck Typing: A type system used in dynamic language. We do not check types at all. Instead, we check for the presence of a given method or attribute.
    ex)
    class bird:
      def fly(self):
        print("bird flying")
    class airplane:
      def fly(self):
        print("plane flying")
    class fish:
      def swim(self):
        print("fish swimming")
    def flying(entity):
      entity.fly()
    
    b = bird()
    a = airplane()
    f = fish()
    flying(b) =>  bird flying
    flying(a) => plane flying
    flying(f) => error, f object has no attribute fly()

33. Abstract class: Allows to create a set of methods that must be created within any child classes built form the abstarct class.
  import abc
  class Person(metaclass=abc.ABCMeta):
    ...
    @abc.abstractmethod
    def drive(self):  # this method must be created within any child class.
      pass
  
34. 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
