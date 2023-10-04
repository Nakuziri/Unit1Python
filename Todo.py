#Asserting an empty variables for a list 
Todo = []
Choices = ''

#Sets the continuation and stopping variables for the while loop
while Choices != 'Stop':

#displays list
    print()
    print('Your current todos are:')
    print(Todo)
    print()
#This gives the user choices to add, delete, or check the list.
    Choices = input('Please select an option. Current choices are "Add" : 1, "Delete" : 2 or "Stop" : 3 to stop:  ')
    print()

#If statement to start off conditionals branch (add varient)
    if Choices == "Add" or Choices == "1" :
#Asks user what they want to add to list
        Addtodo = input('Please type in something to add to your todo list: ')
        Todo.append(Addtodo)
        print()
        print(Addtodo + ' has been added!')
        print()
    
#elif activates based on conditional (del varient)
    elif Choices == "Delete" or Choices == "2" :
#Asks user what index they want to delete
        Deltodo = int(input("Please select the number for the item in the list you'd like to remove: "))
#deletes specified item with -1 to make it user friendly on indexes
        del Todo[Deltodo - 1]
        print("Your selected statement has been deleted!")
        print()

#Segment to stop loop if conditionals are met
    elif Choices == "Stop" or Choices == "3" :
        print('Statement is now stopping')
        print()
#break stops loop
        break

#Repeats the loop if no conditionals are met
    else :
        print('The answer chosen is invalid.')
        print()