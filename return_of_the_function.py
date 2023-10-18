"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def squarerootfun(n):
#return does the process within function (n^2)
    return n**2
#setting a variable to the function to print its result out of the function
something = squarerootfun(8)
#prints assigned variable
print(something)

#setting assert to = to value
assert something == 64
#try handles false assert gracefully
try:
    assert squarerootfun(8) == 9
#except to print out error and move on
except: 
    print('The second assert is wrong')

"""
Task2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
#Setting a function for L and W
def AreaOfRec(length, width):
#Returns values of L and W
    return length * width
carlos = AreaOfRec(9, 10)
#setting true assert for assigned func variable
assert carlos == 90
#setting try for invalid assert
try:
    assert AreaOfRec(10,2) == 89
#except handles error gracefully
except:
    print('AreaOfRec functions second assert invalid.')
#Prints result of function
print(carlos)

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def CelToFah(C) : 
#Making retun do Celcius to Fahrenheight formula 
    return C * (9/5) + 32
convert = CelToFah(10)
#setting correct assert
assert convert == 50.0
#trying invalid assert for graceful error
try:
    assert CelToFah(90) == 7
#error output:
except:
    print('second assert for CelToFah is invalid')

print(convert)

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def avgfun(a):
#sets a variale to sum of parameter
    listtotal = sum(a)
#Returns the sum of all digits in function list    
    return listtotal/len(a)
#variable takes the assigned sum and divides it by the amount of items

print(avgfun([5,7,7,8,9]))

#sets valid assert to check function
assert avgfun([5,7,7,8,9]) == 7.2

#trying invalid assert to handle gracefully
try:
    assert avgfun([5,7,7,8,9]) == 90
#prints out except for assertion error
except AssertionError:
    print('second avg assert is invalid')