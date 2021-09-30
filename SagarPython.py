"""1. A name that is used to denote something or a value is called a variable. 
In python, variables can be declared and values can be assigned to it as follows"""

#Code
x = 2
y = 5
xy = 'Hey'
print (x+y, xy)
# Output: 7  'Hey'

"""2. The print statement can be used in the following different ways :
- print "Hello World"
- print "Hello", <Variable Containing the String>
- print "Hello" + <Variable Containing the String>
- print "Hello %s" % <variable containing the string>"""

#Code
print("""My name is Rajath Kumar M.P.

I love Python.""")
#Output: 
#My name is Rajath Kumar M.P.
#I love Python"""

#Code:
string1 = 'World'
print('Hello', string1)

string2 = '!'
print('Hello', string1, string2)
#Output: 
#Hello World
#Hello World !

#Code:
print("Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug")
#Output: 
# Jan
# Feb
# Mar
# Apr
# May
# Jun
# Jul
# Aug

#Code
print("I want \\n to be printed.")
#Output: I want \n to be printed.

#Code:
x = 10
print(type(x))

s = 'abc'
print(type(s))

value= True
print(type(value))

percent=90.00
type(percent)

#Output:
# <class 'int'>
# <class 'str'>
# <class 'bool'>
# <class 'float'>
