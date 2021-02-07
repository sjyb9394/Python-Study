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