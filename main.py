#Main Execution File
main = True
while main:
    option = str(input("Enter the following to proceed.\n1 - create reservation\nExit - End Transaction\nSelect: "))
    if option == "1":
        print("\nCreating Reservation")
        with open("reservation_create.py") as create:
            exec(create.read())
    if option == "2":
        pass
    if option == "3":
        pass
    
    if option == "Exit":
        main = False
