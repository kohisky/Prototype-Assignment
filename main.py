#Main Execution File
main = True
while main:
    option = str(input("Enter the following to proceed.\n1 - Create Reservation\nExit - Close Menu\nSelect: "))
    if option == "1":
        print("\nCreating Reservation")
        with open("CreateReservartion.py") as create:
            exec(create.read())
    if option == "2":
        pass
    if option == "3":
        pass
    
    if option == "Exit":
        main = False
