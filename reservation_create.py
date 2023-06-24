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
            print(reservationdate)
            slot = int(input("Please select a slot\n1 - 12:00 pm - 02:00 pm\n2 - 02:00 pm - 04:00 pm\n3 - 06:00 pm - 08:00 pm\n4 - 08:00 pm - 10:00 pm"))
            if slot == 1:
                information.append(reservationdate)
                information.append(slot)
                name = str(input("Please enter your Name"))
                information.append(name)
                email = str(input("Please enter your E-mail address"))
                information.append(email)
                phone_number = str(input("Please enter your phone number"))
                information.append(phone_number)
                people = int(input("Please enter the number of people (Maximun is 4 person)"))
                while people >= 5:
                    people = int(input("Please enter the number of people (Maximun is 4 person)"))
                if people <= 4:
                    information.append(people)
                    with open(r"reservation_StudentID.txt", "w") as info:
                        info.write("\n".join(str(item) for item in information))
                        
                    start = False
            if slot == 2:
                pass
            if slot == 3:
                pass
            if slot == 4:
                pass

        else: 
            print("Sorry, reservations must be at least 5 days in advance.")
    except:
        print("Error")


information = []

