"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
#range statement to count from 1 to 11
for x in range(1,11) :
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
#Range counting from 900 to 1001 to have last count be 1000
#puts it in counts of 10
for x in range(900,1001, 10):
    print(x)
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#for loop that counts from 1 to 100 by using 101 in sets of 9
for x in range(1,101,9) :
    print(x)
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#additional variable to count the adding values of range with for variable
a = 0
for x in range(1,11):
#adding a to x for the sums of each iteration done
    a += x
    print(a)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""
#The code is prints lines that that add the "*" by one for every iteration until it reaches 5 because the
#first for loop counts the amount of iterations done with rows which is 5 while the second adds one for
#each iteration done on the first for loop


#Rows assess the amount of lines that'll be used
rows = 5

##Range statement uses the value of rows to measure out the amount of iterations it'll run for (5)
for i in range(rows):
# The j variable makes it so that it adds the 1 for eacht time the first for loop runs an iteration
    for j in range(i + 1):
    #Print statement sends out "*". adds by 1 for each iteration done
    # end statement places a space at shown string
        print('*', end=' ')
    print()