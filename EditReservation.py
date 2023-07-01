from datetime import*

file = open("reservation_StudentID.txt")

#List to contain all initial information from "reservation_StudentID.txt"
list = []
#Reading the data from "reservation_StudentID.txt"
data = file.read()
#Putting the data into a list
list = data.replace("\n", "|").split("|")
list.pop(-1)

start = True
while start:
    try:
        #Using their phone number to find their reservation to edit
        pncheck = input("Please enter your number to find your Reservation.")
        mobilelocation = 4
        #Find/Check the location of the phone number in the list
        while pncheck != list[mobilelocation]:
            mobilelocation += 6
            if IndexError:
                print("Number does not exist within the database.")
                pncheck = input("Please enter your number to find your Reservation.")
                mobilelocation = 4
                continue
            else:
                break

        datelocation = mobilelocation - 4
        slotlocation = mobilelocation - 3
        namelocation = mobilelocation - 2
        emaillocation = mobilelocation - 1
        paxlocation = mobilelocation + 1

        def customerdetails():
            print(f"""
Reservation Details:
Date  : {list[datelocation]}
Slot  : {list[slotlocation]}
PAX   : {list[paxlocation]}
Guest Details:
Name  : {list[namelocation]}
Mobile: {list[mobilelocation]}
Email : {list[emaillocation]}
""")
        customerdetails()

        correct = input("Is this your Reservation? [Yes/No] ").lower()

        while correct != 'yes' and correct != 'no':
            correct = input("Is this your Reservation? [Yes/No]").lower()
        if correct == 'no':
            start = False

        changeselection = input("""
Reservation Changes:
[1] Reschedule Reservation
[2] Change Your Personal Details
[3] No Changes
Select: """).lower()

        while changeselection != '1' and changeselection != '2' and changeselection != '3':
            changeselection = input("""
Reservation Changes:
[1] Reschedule Reservation
[2] Change Your Personal Details
[3] No Changes
Select: """).lower()
        if changeselection == '1':
            while True:
                reservationdate = input("Please insert date (yyyy-mm-dd): ")
                try:
                    reservationdate = datetime.fromisoformat(reservationdate)
                    reservationdate = datetime.date(reservationdate)
                    
                    daycheck = datetime.date(datetime.now() + timedelta(days=5))
            
                    if daycheck <= reservationdate:
                        list[datelocation] = str(reservationdate)
                        break
                    else:
                        print("Booking must be 5 days in advance")
                        continue
                    
                except ValueError:
                    continue            
            
            list[slotlocation] = ("Slot " + str(input("""
Please select a slot
[1] 12:00 pm - 02:00 pm
[2] 02:00 pm - 04:00 pm
[3] 06:00 pm - 08:00 pm
[4] 08:00 pm - 10:00 pm
Select: """)))
            list[paxlocation] = input("PAX (1-4): ")
            customerdetails()

            confirm1 = input("Confirm changes? [Yes/No] ").lower()

            while confirm1 != 'yes' and confirm1 != 'no':
                confirm1 = input("Confirm changes? [Yes/No]").lower()
            if confirm1 == 'no':
                start = False

            numitem = len(list)
            one = 0 
            two = 6
            clear = open("reservation_StudentID.txt", "w")
            clear.write("")
            with open("reservation_StudentID.txt", "w") as edit:
                while one != numitem:
                    edit.write("|".join(list[one:two]) + "\n")
                    one += 6; two += 6
            start = False
            
            

        elif changeselection == '2':
            list[namelocation] = input("Name: ")
            list[mobilelocation] = input("New Phone Number: ")
            list[emaillocation] = input("New E-mail Address: ")
            customerdetails()

            confirm2 = input("Confirm changes? [Yes/No] ").lower()

            while confirm2 != 'yes' and confirm2 != 'no':
                confirm2 = input("Confirm changes? [Yes/No]").lower()
            if confirm2 == 'no':
                start = False

            numitem = len(list)
            one = 0 
            two = 6
            clear = open("reservation_StudentID.txt", "w")
            clear.write("")
            with open("reservation_StudentID.txt", "w") as edit:
                while one != numitem:
                    edit.write("|".join(list[one:two]) + "\n")
                    one += 6; two += 6
                
            start = False

        elif changeselection == '3':
            start = False

    finally:
        again = input("Would you like to edit your reservation? [Yes/No] ").lower()

        while again != 'yes' and again != 'no':
            again = input("Would you like to edit your reservation? [Yes/No]").lower()

        if again == 'no':
            start = False
file.close()


"""
This is used to rearrange to check date and slot
list = []
list = data.split("\n")
list.pop(-1)
list.sort()
"""