'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
x = 20 
if x == 10 and x > 10 :
    print ('True')
else: 
    print('False')

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
Age = 20 
Status = 'Student'

if Age == 18 or Status == 'Student' :
    print ('Congrats! You only pay 10')
else: 
    print('pay up 20 >:(')

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
Fruits = ['Apple', 'Pear', 'Orange', 'Kiwi', 'Peach']

FruitName = input("Enter a fruit name: ")

if FruitName in Fruits :
    print("Yes, that fruit is in the list.")
else:
    print('No, that fruit is not in the list.')

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
YearV = input('Enter a year: ')
 
if int(YearV) % 4 == 0 and int(YearV) % 100 == 0;
    print('This is a leap year AND a century')
else :
    print('False')

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
packWeight = int(('enter package weight'))
zone = input('insert location to ship to')

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''
angle = input('enter a triangle angle')
angle2 = input('enter a second angle')
angle3 = input('enter a 3rd angle')

if angle or angle2 or angle3 =