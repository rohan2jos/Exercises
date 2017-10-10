# Exercises
Contains exercises and examples


## Question: Python provides a built-in function called len that returns the length of a string, so
the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a parameter and prints the
string with enough leading spaces so that the last letter of the string is in column 70 of the display.
## Solution: https://github.com/rohan2jos/Exercises/blob/master/right_justify.py

## Question: A function object is a value you can assign to a variable or pass as an argument. For
example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f):
f()
f()

Here's an example that uses do_twice to call a function named print_spam twice.
def print_spam():
print 'spam'
do_twice(print_spam)
1. Type this example into a script and test it.
## Solution: https://github.com/rohan2jos/Exercises/blob/master/do_twice_1.1.py
2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
function twice, passing the value as an argument.
## Solution: https://github.com/rohan2jos/Exercises/blob/master/do_twice_1.2.py
3. Write a more general version of print_spam, called print_twice, that takes a string as a
parameter and prints it twice.
## Solution: https://github.com/rohan2jos/Exercises/blob/master/do_twice_1.3.py
4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
argument.
## Solution: https://github.com/rohan2jos/Exercises/blob/master/do_twice_1.4.py
5. Define a new function called do_four that takes a function object and a value and calls the
function four times, passing the value as a parameter. There should be only two statements in
the body of this function, not four
## Solution: https://github.com/rohan2jos/Exercises/blob/master/do_twice_1.5.py
