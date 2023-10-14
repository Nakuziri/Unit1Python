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
    

"""
Task2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
#Setting a function for L and W
def AreaOfRec(length, width):
#Returns values of L and W
    return length * width
carlos = AreaOfRec(9, 10)
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
print(convert)

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
#Setting up multiple asserted values within function
def avgfun(a,b,c,d,e,f):
#Returns the sum of all six digits
    return a + b + c + d + e +f
#variable takes the assigned sum and devides it by the amount of items
avg = avgfun(1,2,3,4,5,6) / 6
print(avg)

