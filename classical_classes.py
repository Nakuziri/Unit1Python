
"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
#people class holds methods for attributes of name and age
class People:
#initializing name and age attribues
    def __init__(self, name, age):
        self.name = name
        self.age = age

# introductory method uses previous attribues
    def Intro(self) :
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old.')

#sets an object for arguments in class
Thug = People("Zesty Quagmire", 17) 

#Calls class method through object with inserted arguments
Thug.Intro()

"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
#Sets Animal class with method
class Animal():
    def speak(self):
        print('Hello')

#Animal Subclass for dogs
class Dogs(Animal):
    def speak(self):
        print('Woof >:(')

#Animal Subclass for cats
class Cats(Animal):
    def speak(self):
        print('MEOW~!!!!!!')

#sets objects for all 3 classes
ani1 = Animal()
ani2 = Dogs()
ani3 = Cats()

#Calls all 3 objects on their associated class methods
ani1.speak()
ani2.speak()
ani3.speak()


"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

#Sets a BankAccount class
class BankAccount( ):
#initializing Balance and Owner attributes
    def __init__ (self, Balance, Owner):
        self.Balance = Balance
        self.Owner = Owner

#Sets Balance display method using blance attribute
    def CurrentBalance(self): 
        print('The current balance is: ' + str(self.Balance))
    
#Depositing method adds values method argument to balance
#deposit perameter set in method
    def depositing(self, deposit):
        #setting balance = to new value
        self.Balance = self.Balance + deposit 
        print("Balance after deposit is: " + str(self.Balance))

#Withdraw method subtracts assigned withdraw value from balance
#withdraw perameter set in method
    def withdrawing(self, withdraw):
        #setting balance = to new
        self.Balance = self.Balance - withdraw
        print("Balance after withdraw is: " + str(self.Balance))
    
#Object to class with assigned arguments
BankStuff = BankAccount(69, 'Booger Boy 29')

#Calls CurrentBalance method in class with object
BankStuff.CurrentBalance()

#Calls deposit method in class with oject and assigned argument
BankStuff.depositing(9000)

#Calls withdraw method in class with object and setted argument
BankStuff.withdrawing(3667)