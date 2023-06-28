file = open("reservation_StudentID.txt")

#List to contain all initial information from "reservation_StudentID.txt"
list = []
empty = []
#Reading the data from "reservation_StudentID.txt"
data = file.read()
#Putting the data into a list
list = data.replace("\n", "|").split("|")

pncheck = input("Please enter your number to find your reservation to edit.")
location = 4

while pncheck != list[location]:
    location += 6
    
print(location)

list[location] = input("What will you like to change your phone number to?")

numitem = len(list) - 1
one = 0 
two = 6
clear = open("reservation_StudentID.txt", "w")
clear.write("")
with open("reservation_StudentID.txt", "w") as edit:
    while one != numitem:
        print(list[one:two])
        edit.write("|".join(list[one:two]) + "\n")
        one += 6; two += 6
    edit.write(list[-1])


file.close()
