#Main Execution File
import os 

def NavigateMenu():
    print("""
     __                                         _____                       _____                              
    / () |)    _,   ,_          o        _,    () ||)                 _    () | ,_   _, _|__|_  _   ,_  o  _,  
   |     |/\  / |  /  | /|/|/|  | /|/|  / |       ||/\  |  | /|/|/|  |/       |/  | / |  |  |  / \_/  | | / |  
    \___/|  |/\/|_/   |/ | | |_/|/ | |_/\/|/    (/ |  |/ \/|/ | | |_/|_/    (/    |/\/|_/|_/|_/\_/    |/|/\/|_/
                                         (|               (|                     
                                                                       
    """)
    print(" {:=^110}".format("🌹 Welcome to Charming Thyme Trattoria! 🌹"))
    print("")
    print(" {:^112}".format("[1] Book a reservation   🍽️"))
    print(" {:^112}".format("[2] Delete a reservation 🗑️"))
    print(" {:^112}".format("[3] Edit a reservation   ✍️"))
    print(" {:^112}".format("[4] Display Reservations 🗒️"))
    print("{:^112}".format("[5] Recommend me a dish! 🍴"))
    print("{:^112}".format("[Exit] Close Transaction ✅"))


main = True
while main:
    os.system("cls")
    NavigateMenu()
    option = str(input(f"{' '*43}Select: "))
    
    if option == "1":
        os.system("cls")
        print("\nMaking Reservation")
        with open("AddReservation.py") as add:
            exec(add.read())
    
    if option == "2":
        os.system("cls")
        print("\nCanceling Reservation")
        with open("CancelReservation.py") as cancel:
            exec(cancel.read())
    
    if option == "3":
        os.system("cls")
        print("\Editing Reservation")
        with open("EditReservation.py") as edit:
            exec(edit.read())
    
    if option == "4":
        os.system("cls")
        print("\Displaying Reservation")
        with open("Display.py") as display:
            exec(display.read())
    
    if option == "5":
        os.system("cls")
        print("\Recommending a Dish")
        with open("MealRecommendation.py") as reco:
            exec(reco.read())
    
    if option == "Exit":
        main = False
