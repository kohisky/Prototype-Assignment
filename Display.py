start = True
while start:
    # reading the file
    data = open("reservation_StudentID.txt", "r").read()
    print(data)
    #this input is to hold the display til the user is done checking reservation
    done = input()
    start = False