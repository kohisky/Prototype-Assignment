import random
#TODO ask user how many to generate or if surprise then it will generate one
start = True
while start:
    with open("menuItems_StudentID.txt") as menulist:
        recommend = menulist.readlines()
    randomize = random.randint(0, 7)
    print("Your recommendation is", recommend[randomize])

    again = input("Would you like another recommendation? [Y/N] ").lower()

    while again != 'n' and again != 'y':
        again = input("Would you like another recommendation? [Y/N]").lower()

    if again == 'n':
        start = False
