Simple Helpful Python codes
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

5. Use \ for printing certain symbols.
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

8. List
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
   
