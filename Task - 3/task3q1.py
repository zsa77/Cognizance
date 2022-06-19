import numpy as np
i=int(input("Enter First Number: "))
j=int(input("Enter Second Number: "))
Z = np.arange(i,j+1)
Z0 = np.zeros(len(Z) + (len(Z)-1)*(5))
Z0[::6] = Z
print(Z0)