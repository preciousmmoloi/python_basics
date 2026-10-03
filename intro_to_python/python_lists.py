
# LIST - number of elements belonging to the same variable

family_members = ['Precious', 'Sannah', 'Dorah', 'Bennedict', 'Phillip']

print(family_members[0] + ' is the daughter of ' + family_members[4])

member_details = [['Precious', 27, 'Cape Town', 'Mazda CX-5'], ['Bennedict', 26, 'Vanderbijlpark', 'Volkswegen'], ['Dorah', 20, 'Pretoria', 'Suzuki']]
print(member_details[0])
print(type( member_details))

member_details[0][2] = 'Harrismith' #updates a value in the 1st element
print(member_details[0])

name = 'Precious'
surname = 'Moloi'
age = 28

person = [name, surname, age, 'Mazda CX-5'] #calling the variable, calls the value
print(person[0])

ageandcar = person[2:4]

print(ageandcar)

# SUBSETTING - Creati gout list from a present list
# slice - getting a piece of the list by specfifying the start to the end index with the end index excluded

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[ : 3])
print(numbers[ 2: ])
print(numbers[-2]) #starts from the back to the front

# LIST MANIPULATION - updating element values, adding elements, removing elements

numbers[0:2] = [100, 90] #updating using list slice
print(numbers)

del numbers[0] # deletes the element o that index and the other elements move 1 element forward

print(numbers)


numbers = numbers + [900, 800, 700] #attaches a list to another list

print(numbers)

#COPING A LIST, use below methods -> using the assignment character assigns the old list to a new variable and can therefore change or update the same list

y = list(numbers)
z = numbers[:] # copy from start to finish

