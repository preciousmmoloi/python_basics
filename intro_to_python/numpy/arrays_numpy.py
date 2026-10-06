import numpy as np

ages = [17, 24, 27, 53]
np_ages = np.array(ages)

np_list = np.array([123, 1234, 12345, 123456])

''' calculate age in 10 years of everyone in the list without going over each one individually'''
in_ten_years = np_ages + 10 #using the numpy list

print(in_ten_years)


#volume and fees --> total fees on invoice

volume = [2, 5, 8, 1, 6, 3]
np_volume = np.array(volume)

fees = [1.5, 3.0, 1.8, 9, 3.5, 0.3 ]
np_fees = np.array(fees)


display_value = np_volume * np_fees 

print("Display value for each volume is: ",display_value)

print(np_volume[np_volume > 3]) #returns a list 
print(np_volume[0]) 
print(np_volume < 3) #boolean list return