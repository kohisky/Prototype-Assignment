from datetime import*

information = []
start = True
while start:
    try:
        date_components = input('Enter a date formatted as DD-MM-YYYY: ').split('-')
        day, month, year = [int(item) for item in date_components]
        reservationdate = date(year, month, day)

        check = datetime.date(datetime.now() + timedelta(days=5))

        if check <= reservationdate:
            slot = int(input("Please select a slot\n1 for 12:00 pm - 02:00 pm\n2 for 02:00 pm - 04:00 pm\n3 for 06:00 pm - 08:00 pm\n4 for 08:00 pm - 10:00 pm\nSelect: "))
            if slot >= 1 and slot <= 4:
                information.append(reservationdate)
                information.append("Slot " + str(slot))
                name = str(input("Please enter your Name: "))
                information.append(name)
                email = str(input("Please enter your E-mail address: "))
                information.append(email)
                phone_number = str(input("Please enter your phone number: "))
                information.append(phone_number)
                people = int(input("Please enter the number of people (Maximun is 4 person): "))
                while people >= 5 and people <= 0:
                    people = int(input("Please enter the number of people (Maximun is 4 person): "))
                if people <= 4 and people >= 1:
                    information.append(people)
                    with open("reservation_StudentID.txt", "a") as info:
                        info.write("|".join(str(item) for item in information) + "\n")
                    start = False
            else:
                print("Invalid Time Slot")
                start = False
        else:
            print("Sorry, reservations must be at least 5 days in advance.")
    except:
        print("Error")
        
    
    finally:
        again = input("Would you like to make another reservation? [Y/N] ").lower()

        while again != 'y' and again != 'n':
            again = input("Would you like to make another reservation? [Y/N]").lower()

        if again == 'n':
            start = False

