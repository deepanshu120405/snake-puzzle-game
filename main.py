import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([1,-1,0])
youstr = input("Enter your choice:")
youDict = {"s": 1,"w": -1,"g": 0}
reverseDict = {1 : "Snake", -1 : "Water", 0 : "Gun"}
you = youDict[youstr]
 # By now we have 2 number {variable}, you and computer
print (f"Your choice {reverseDict[you]} \n Computer choice {reverseDict[computer]}")
if (computer == you):
    print("ITS Draw !")
    
else:
    if ( computer == 1 or you == 0):
        print("You Win!")
    elif (computer == 1 or you == -1):
        print( "You lose!")
    elif (computer == 0 or you == 1):
        print("You lose!")
    elif (computer == 0 or you == -1):
        print( "You Win!")
    elif (computer == 1 or you == 0):
        print("You Win!")
    elif (computer == 1 or you == -1):
        print("You Lose!")
    else:
        print("Something went wrong!:")
