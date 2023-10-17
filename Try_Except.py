#Using try to test the specfic segmet of code
try:
    age = int(input('Enter your age: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
#This outputs a result if the code reaches an error 
except:
    print('problem A')
#A second try to check this specific error segment
try:
    faveNum = int(input('What is your favorite number: '))
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
    print('Problem B')

