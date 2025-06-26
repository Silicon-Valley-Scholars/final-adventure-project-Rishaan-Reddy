import random

health = 100
inventory = []  # List to store collected items

def choose_character():
    choice = input("Your name is James or Aaron. Do you want to be James or Aaron? Type 'James' or 'Aaron': ")
    while choice != "James" and choice != "Aaron":
        print("Please type 'James' or 'Aaron'.")
        choice = input("Do you want to be James or Aaron?")
    return choice

choice = choose_character()
if choice == "James":
    print("You are James, a clever person. You have", health, "health points.")
elif choice=="Aaron":
    print("You are Aaron, a brave adventurer. You have", health, "health points.")
print("You are in a dark cave, you can see a light at the end of the cave and deeper inside the cave you can hear a lot of noise that sounds like animals. It sounds like chickens and you think it is tasty food but you are not sure. Do you want to go towards the light or stay in the cave?")
choice = input("Type 'light' to go towards the light or 'stay' to stay in the cave: ")
if choice == "light":
    print("You walk towards the light and find a beautiful garden. You feel safe and happy and end up with", health, "health points.")
else: 
    print("You stay in the cave and hear the noise getting louder. Suddenly, a bear appears and chases you out of the cave!")
    choice = input("Do you want to run or fight the bear? Type 'run' to run or 'fight' to fight: ")
    if choice.lower() == "run":
        print("You run as fast as you can and escape the bear. You find yourself back at the entrance of the cave.")
    elif choice.lower() == "fight":
        health -= 70
        print("You bravely fight the bear, and it almost overpowers you. You manage to injure it, but you are also injured in the process. You have", health, "health points left.")
        print("You find a sword and a shield on the ground. One of your hands is free and the other is broken, do you want to pick up the sword or the shield?")
        choice = input("Type 'sword' (50 attack, 10 shield) to pick up the sword or 'shield'(20 attack and 70 shield) to pick up the shield: ")
        if choice.lower() == "sword":
            inventory.append("sword")
            health -= 20
            print("You pick up the sword and fight the bear. You manage to defeat it and escape the cave with", health, "health points left.")
            print("Your inventory:", inventory)
        else:
            inventory.append("shield")
            health = 30
            print("You pick up the shield and use it to block the bear's attacks. You manage to escape the cave, but you are injured with only", health, "health points left.")
            print("Your inventory:", inventory)
            print("You find a way out of the cave and see the light again. You walk out of the cave and find yourself stranded on a deserted island.")
            print("You find an apple tree and a cave on the island. Do you want to eat an apple (+30 health points) or go into the cave?")
            choice = input("Type 'apple' to eat an apple or 'cave' to go into the cave: ")
            if choice.lower() == "apple":
                inventory.append("apple")
                health += 30
                print("You eat an apple and feel refreshed. You gain 30 health points and now have", health, "health points.")
                print("Your inventory:", inventory)
            else:
                print("You enter the cave and find a chicken coop with chickens inside. Do you want to eat a chicken (+60 health points) or leave the coop?")
                choice = input("Type 'eat' to eat a chicken or 'leave' to leave the coop: ")
                if choice.lower() == "eat":
                    health += 60
                    print("You eat a chicken and feel full. You gain 60 health points and now have", health, "health points.")
                else:
                    print("You leave the coop and find a river. You can drink from the river to regain some health.")
                    choice = input("Type 'drink' to drink from the river or 'ignore' to ignore the river: ")
                    if choice.lower() == "drink":
                        health += 10
                        print("You drink from the river and feel refreshed. You gain 10 health points and now have", health, "health points.")
                    else:
                        print("You ignore the river and continue exploring the island.")
            print("You see a boat in the distance. Do you want to swim to the boat or wait for it to come to you?")
            choice = input("Type 'swim' to swim to the boat or 'wait' to wait for it to come: ")
            if choice.lower() == "wait": 
                print("You wait for the boat to come to you but it never comes. You are left on the island and die of thirst and hunger.")
            else: 
                print("You swim to the boat but you were sadly too slow at swimming due to lack of food.")
                print("You swim back to the island and find a different cave that is near the coast to rest in.")