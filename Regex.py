import re

#Take users data

data = input("Please enter your first and last name: ")


#convert all first name last names into a tomEDWARDS format

#Split word 

data = re.split("\s",data)

#Capatalize last word

data[1] = data[1].upper()

#Region the words

data = data[0] + data[1]


print(data)



