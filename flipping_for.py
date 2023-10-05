"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""
# a simple for loop with a variable that prints out every character in a string sepratly
w = 'hverjgrekbverjgjbre'
for character in w :
    print (character)
"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""
#a seprate variable is used to add all the values of list together, giving a final sum 
v = 0
nu = [2,2,2,3,4,5,6,7,8,6,4,43,3,3,5,6,7]
for n in nu :
    v += n
    print(v)
"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""
#Sen value for sentence 
sen1 = 'Today I have turned to a set amount of years which was great because I am now older.'
#the slpit with spacing statement splits words on every space and len counts the characters of the word
sen1 =sen1.split(' ')
for letter in sen1 :
    print(len(letter))
    
"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""
#I noticed that the keys were the only thing printed and not the values which was far from what i expected
# an objects list that prints out ever key only
Ball = {
    'color' : 'red',
    'size' : 'x-large',
    'bouce lvl' : 'Very large',
    'material' : 'rubber'
}
for desc in Ball :
    print(desc)
