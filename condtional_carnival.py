'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''

number = int(input('please enter a number'))
 
number = number % 2

if number == 0:
    print('this number is even')
else:
    print('This number is odd')


'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
nums = int(input('please enter a number'))

if nums > 0 :
    print('This is a positive value')
elif nums < 0 :
    print('This is a negative value')
elif nums == 0 :
    print('This is a zero value')
else :
    print ('invalid value')


'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
nl = [5,2,6]

biggestValue = max(nl)
print('The biggest value is: ' + str(biggestValue))

'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
leaps = int(input('what year is it right now?: '))
leaps = leaps % 4 
if leaps == 0 :
    print('This is a leap year')
else:
    print('This is not a leap year')
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.
EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''
consonant = [ 'b','B','c', 'C', 'd', 'D', 'f', 'F','g', 'G','h', 'H','j','J', 'k', 'K','l', 'L','m', 'M','n', 'N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x', 'X','z', 'Z']
Vowel = ['A','a', 'E','e', 'I','i', 'O','o', 'U','u', 'Y','y', 'W','w']

ltrChec = input('please enter a letter')
if int(ltrChec) :
    print ("This is a number (INVALID)")
elif float(ltrChec) :
    print ("This is a float number (INVALID)")
elif ltrChec == any(consonant) :
    print('This is a consonant')
elif ltrChec == any(Vowel) : 
    print('This character is a vowel')
else :
    print('invalid')
