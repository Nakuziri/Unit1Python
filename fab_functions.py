# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

#defining function for name
def greet(name):
    print('Hello' + name)
#Choosing name to display
greet("Xavier")

# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

#defining a two variable function
def sum_numbers(a, b):
#printing sums and inputting sums to functions 
    print(a + b)
sum_numbers(200, 2000)

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.


def factorial(n): 
#Making a variable to get sum of factorial
    bc = 1 
#Creating a while loop for factiorial
    while n > 1:
#adding values to get new factorial value
        bc = n * bc 
#counts until loop conditons met
        n -= 1 
    print(bc)
factorial(10)

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def is_even(num):
    #if statement to find even and odd values
    if num % 2 == 0:
        print('True')
    else:
        print('False')
is_even(91)

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.

#creating a function for length & width
def Calculate_area(length, width) :
#printing the two variables to calculate total area
    s = length * width
    print(s)
Calculate_area(10, 15)
