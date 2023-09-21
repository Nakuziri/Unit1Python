#Task 1: Create a list
#Create a list with 4 elements and print it.

# I started off by creating a simple list containing games I like and labled the list as "Games"

Games = ["Elden Ring", "Overwatch", "Roblox", "Brawlhalla"]

#Task 2: Add Element to a List
#Add an element to the end of the list. Print the updated 
#list.

#For this task I specifically used the append statement to add another specific game item towards the end of the list

Games.append("Spiderman")
print(Games)

#Task 3: Remove Element from a List
#Remove a specific element from the list. Print the 
#updated list.

#In this task I specifically used the "remove" statement (not to be confused for the "del" statement) to remove an item by name from my Games list

Games.remove("Spiderman")
print(Games)

#Task 4: Modify Element in a List
#Modify an element at a specific index with a new value. 
#Print the updated list.

#In this task I modified the 3rd item in my list by chaning the string item "Roblox" to "Roblox_Mid" by getting the specific item number then printing it

Games[2] = "Roblox_Mid"
print(Games)

#Task 5: Append Multiple Elements to a List
#Append multiple elements to the end of the list. Print 
#the updated list.

#For this task I did multiple append statements to add a series of games into my games list

Games.append("SmashBros")
Games.append("Phasmophobia")
print(Games)

#Task 6: Delete Element at a Specific Index
#Delete an element at a specific index. Print the updated 
#list.

#In this task I specially used the delete statement to delete an item within a list with the item number of the list

del Games[4]
print(Games)

#Task 7: Subsetting lists
#Create a new variable equal to the first 2 items of your list
#Then print out the new variable

#For this task I took a specific portion of my list (the first two items) and stored the output (The two list items) into a new veriable labled as game_B then printed that output

game_B = ( Games[0:2])
print(game_B)

#Task 8: Extend a List
#Extend the list with the elements of another list. Print 
#the updated list.

#For this task I used the perviously created varible that took a portion out of my original games list and added it back to the original games list by extending the list and printing the output of the both of them combined as a new variable known as addGame

addGame = Games + game_B
print(addGame)