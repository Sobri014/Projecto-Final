# ex1 - Example: Taking input using sys.stdin in a for-loop
import sys
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')
    print("Exit")
# ex2 - Read Input From stdin in Python using input()
# this accepts the user's input
# and stores in inp
#inp = input("Type anything")
# prints inp
#print(inp)
# ex3 - Example 1: Reading multiple files by providing file names in fileinput.input()function argument
import fileinput
with fileinput.input(files=('sample.txt', 'no.txt')) as f:
    for line in f:
        print(line)

# ex4 - Example 2: Reading multiple files by passing file names from command line usingfileinput module
import fileinput
#for f in fileinput.input():
#    print(f)

import sys
def print_to_stderr(*a):
# Here a is the array holding the objects
# passed as the argument of the function
    print(*a, file=sys.stderr)
    print_to_stderr("Hello World")
# ex2 - Method 2: Using Python sys.stderr.write() function
import sys

print("Example 1")
print("Example 2", file=sys.stderr)
sys.stderr.write("Example 3")
# ex3 - Method 3: Using Python logging.warning function
import logging

logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
log.warning('Error: Hello World')

# ex1 - Method 1: Using Python sys.stdout method
import sys
def print_to_stdout(*a):
# Here a is the array holding the objects
# passed as the argument of the function
    print(*a, file=sys.stdout)
    print_to_stdout("Hello World")
# ex2 - Method 2: Using Python print() function
    print( "Hello GeeksforGeeks" )

# ex3 - Method 3: Using Python sys.stdout.write() function
import sys
a = 11
print(a)
print(a, file=sys.stdout)
sys.stdout.write(a)