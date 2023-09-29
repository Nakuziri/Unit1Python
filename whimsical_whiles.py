"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
i = 0
while i < 11 :
   print(i)
   i += 1
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
i = 10 
while i > 0:
  print (i)
  i -= 1

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
""" 
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = ''
while password != 'apples':
   password = input('Guess the password: ')
   if password == 'apples':
      print('Nice!')
   else :
      print('Try again :(')

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
c = 'Start'
while c != 'Stop':
    value = input('Give me a number: ')
    val2 = input('give me a second number: ')
    print(int(value) + int(val2) )
    
    
    c = input("Type 'Stop' to stop or 'go' to continue: ")
    if c == 'Stop' :
        break

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""