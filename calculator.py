##I started off by creating two input variables which will be holding my two values labled as "One" and "Two".

One = input('Please input your first numerical value: ')
print()
Two = input('Please input your first numerical value: ')

##Afterwords I continued by stating the possible mathematical notations that this calculator supports.
print()
print('Possible mathematical notations are:')
print('1.Addition: +')
print('2.Subtraction: -')
print('3.Multiplication: *')
print('4.Division: /')
print('5.Floor Division: //')
print('6.Exponential: **')
print('7.Remainder: %')
print('')

##I Also Created a variable named as "MathSym" which holds the mathematical symbol that will be used on the two numerical values.
MathSym = input("Select Which mathematical notation you'd like to use: ")
print()

##Before going into the actual math process, I relabed the two variables as "VariableOne" and "VariableTwo" 
#so that I could change their data types to intergers
ValueOne = int(One) 
ValueTwo = int(Two)

##I then continued to make the if statement followed by multiple elifs to make the actual math function. 
##I exclusively used one if statement with multiple elifs so that only one conditional statement will be fufilled.
if MathSym == "+":
    print(ValueOne + ValueTwo) 

elif MathSym == "-" :
    print(ValueOne - ValueTwo)

elif MathSym == "*":
    print(ValueOne * ValueTwo)

elif MathSym == "/":
    print(ValueOne / ValueTwo)

elif MathSym == "//":
    print(ValueOne / ValueTwo)

elif MathSym == "**":
    print(ValueOne ** ValueTwo)

elif MathSym == "%":
    print(ValueOne % ValueTwo)

##final else statement just to state that if none of the previous conditionals for 
#a mathematical symbol were met, the notation would be invalid.

else:
    print('The selected mathematical notation is INVALID')