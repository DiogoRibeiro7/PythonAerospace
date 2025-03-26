"""
Dictionary:
IVR - Induced Velocity Ratio
CVR - Climb Velocity Ratio

Description:
This code demonstrates a function that calculates the Induced Velocity Ratio 

Conclusion:


Sources:


Libraries required:
 - matplotlib
 - numpy
"""

import matplotlib.pyplot as plt
import numpy as np

def Induced_Velocity_Ratio(x):
    """Returns Induced Velocity Ratio based on 3 conditions
    
    req: x value
    """

    # Initialize an array to store IVR
    cl = np.zeros_like(x)

    # Apply the conditional sine model
    condition1 = np.logical_and(-np.inf <= x, x <= -2)
    condition2 = np.logical_and(-2 <= x, x <= 0)
    condition3 = np.logical_and(0 <= x, x <= np.inf)

    # Apply the functions based on the conditions
    
    cl[condition1] = ((-1/2)*x[condition1])-((1/2)*np.sqrt((x[condition1]**2)-4)) # for CVR between -4 and -2
    cl[condition2] = 0.974 - (1.125*x[condition2]) - (1.372*(x[condition2]**2)) - (1.718*(x[condition2]**3)) - (0.655*(x[condition2]**4)) # for CVR between -2 and 0
    cl[condition3] = ((-1/2)*x[condition3])+((1/2)*np.sqrt((x[condition3]**2)+4)) # for CVR between 0 and 4

    
    return cl 

#X axis between -4 and 4
climbVelocityRatio = np.linspace(-10, 10, 1000)

#Calculates Induced Verlocity Ration based on 
yValues = Induced_Velocity_Ratio(climbVelocityRatio)

#Plot the values
plt.plot(climbVelocityRatio, yValues, color="red")


#Print the values (for debugging reasons)
print("Climb Velocity Ratio:", climbVelocityRatio)
print("Induced Velocity Ratio:", yValues)

#Title and Axis Labels
plt.xlabel("Climb Velocity Ratio, Vc/vh", fontsize=12)
plt.ylabel("Induced Velocity Ratio, vi/vh", fontsize=12)
plt.title("Induced Velocity Variation", fontsize=14)

#Define y limits
plt.ylim(0,3)
plt.xlim(-4,4)

#Create a grid
plt.grid(True, which='both')

#Show the window
plt.show()