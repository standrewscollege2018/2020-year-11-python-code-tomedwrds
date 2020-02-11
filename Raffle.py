import random
import time

print("Welcome to the raffle program")

#Take input for the item and its worth
item = input("What is the item being raffled: ")

setting_worth = True

#Error checking to prevent a string being entered as worth
while setting_worth:
    try:
        worth = int(input("What is the {} worth - dont enter the $: ".format(item)))
        setting_worth = False
    except:
        print("Please enter a valid value")
    

#Take the entrants
entrants = []

entrant_names = True

while entrant_names:
    
    name = input("Enter name of entrant: ")
    
    if name == "end" :
        entrant_names = False
    else :
        entrants.append(name)
    

print("There are {} people entered".format(entrants.__len__()))


#Select the winner randomly
winner = random.randint(0,entrants.__len__()-1)

print("Selecting winner...")

time.sleep(1)


print("And the winner for the {}, valued at ${} is...... {}".format(item,worth,entrants[winner]))


    
    