'''
Differences between python2 and python3
Python2 Python3
->Python 2’s print statement has been replaced by the print() function
   print 'Hello, World!' print('Hello, World!')
->Integer division
  This change is particularly dangerous if you are porting code, or if you are executing Python 3 code in Python 2,since the change in integer-division behavior can often go unnoticed (it doesn’t raise a SyntaxError).
  3 / 2 = 1 3 / 2 = 1.5
->In python2 strings are stored in ASCII by default where as in python3 strings are unicode by default
->xrange() of Python 2.x doesn’t exist in Python 3.x
   for x in xrange(1, 5):
    print(x),
   for x in range(1, 5):
    print(x),

   Output in Python 2.x
    1 2 3 4 1 2 3 4
   Output in Python 3.x
    NameError: name 'xrange' is not defined
'''

#Input the string Python as a list of characters from console, delete at least 2 characters, reverse the resultant string and print it

user = input('enter a string')
y=int(input('enter the number of characters to be deleted'))
a = user[y+1:]
print(a)
print(a[::-1])

#Take two numbers from user and perform arithmetic operations on them

x= int(input('enter a number'))
y= int(input('enter another number'))

print(x+y)
print(x-y)
print(x*y)
print(x%y)
print(x/y)
print(x**y)
print(y**x)

# Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex

user = input("enter a sentence which consists the word python atleast once")
if user.find('python'):
    print('success')
print(user.replace('python', 'pythons'))



