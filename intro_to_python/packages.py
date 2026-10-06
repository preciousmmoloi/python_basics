import numpy as np

""" PACKAGES --> Code written by others can you can use for your ownn specific use-cases to solve own problems with own code

 scripts found in those packages are called MODULES. Each module has specific functions, methods and types 
 
examples of packages: numPy(working with arrays), matplotlib(data visualization), scikit-learn (ML) """



ages = [17, 25, 27, 53, 53]


np.array(ages)

print(np.array(ages))

''' EXAMPLE OF IMPORTING AN ENTIRE PACKAGE

import math as m 

# Calculate C
C = 2 * 0.43 * m.pi (pi is a function from the math package)

# Calculate A
A = m.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

'''

''' EXAMPLE OF IMPORTING JUST A SPECFIC FUNCTION FROM A PACKAGE
from math import pi

C = 2 * 0.43 * pi
A = pi * 0.43 ** 2

NO NEED TO REFERENCE MATH or M

'''

# from scipy.linalg import inv as my_inv -> the imported function can also be given an aliasing