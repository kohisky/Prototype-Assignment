import datetime
my_file = open("reservation_StudentID.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.replace("\n", "|").split("|")
print(data_into_list)
my_file.close()

date_list = str(data.split(datetime.date))