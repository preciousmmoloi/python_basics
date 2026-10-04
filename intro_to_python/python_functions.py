 # FUNCTIONS --> PIECES OF REUSABLE CODE THAT PERFORM A PARTICUALR TASK

from random import random

fam = [90, 20.8456786486, 50, 60, 70, 100]

# built in functions --> python

print(max(fam))

rounding = round(fam[0],2)

print(rounding)

print(len(fam))

number = 4

# the help() function can help us understand hat a fucntion does

print(pow(number, 2))

sortedlist = sorted(fam, reverse = True) #sort in descending
print(sortedlist)

#METHODS --> specific functions that apply and belong to certain python objects

name = 'precious'

print(name.capitalize())

print(fam.index(100))

people = ['Precious', 'Moloi', 'Precious']
print(people.index('Moloi') + 1) #gets the index number of the specified string in the list

print(people.count('Precious')) #counts how many similar names are in the list

names = name.replace('p', 'Z')
print(names.capitalize())
print(names.upper())

people.append(input()) #asks and adds a name to the list 
print(people)

people.remove(input()) #removes the first element that matches the input
print(people.reverse())