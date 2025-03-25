"""
Description:
This code demonstrates a function that calculates the Coefficient of Lift (CL)
for an aerofoil as a function of its Angle of Attack (AoA), measured in degrees. The purpose
of this model is to illustrate how the lift coefficient changes with increasing AoA. As the
AoA increases, the airflow over the wings becomes more turbulent, and eventually, the aerofoil
begins to experience stall. This results in a reduction of the lift coefficient as the 
angle of attack exceeds a critical threshold, simulating the aerodynamic behavior of 
the wing during stall. 

Sources:
https://en.wikipedia.org/wiki/Lift_coefficient
https://www.flight-training-made-simple.com/post/the-lift-formula
https://aviation.stackexchange.com/questions/64490/is-there-a-simple-relationship-between-angle-of-attack-and-lift-coefficient
https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/liftco.html

Libraries required:
 - matplotlib
 - numpy
"""
#Still W.I.P

import matplotlib.pyplot as plt
import numpy as np

def Lift_Coefficient(x):
    """Returns Lift Coefficient based on AoA sine model
    
    req: x value
    """
    # Convert x to radians for all values
    radX = np.radians(x)

    # Initialize an array to store lift coefficients
    cl = np.zeros_like(x)

    # Apply the conditional sine model
    condition1 = np.logical_and((np.pi/8) <= radX, radX <= (7*np.pi)/8)
    condition2 = ~condition1

    # Apply the sine functions based on the conditions
    cl[condition1] = np.sin(2 * radX[condition1])  # for AoA in range [π/8, 7π/8]
    cl[condition2] = np.sin(6 * radX[condition2])  # for AoA outside that range
    
    #Convert x to radians for all values
    radX = np.radians(x)

    # Initialize an array to store lift coefficients
    cl = np.zeros_like(x)

    # Apply the conditional sine model
    condition1 = np.logical_and((np.pi/8) <= radX, radX <= (7*np.pi)/8)
    condition2 = ~condition1  # Everything else (outside the range)

    # Apply the sine functions based on the conditions
    cl[condition1] = np.sin(2 * radX[condition1])  # for AoA in range [π/8, 7π/8]
    cl[condition2] = np.sin(6 * radX[condition2])  # for AoA outside that range

    return cl 

"""
#Calculates aspect ratio for the AW109SP Helicopter

rotorRadius = 5.5
chordLength = 0.2
aspectRatio = rotorRadius/chordLength """

#X axis between 0 and 180 degrees
alphaDeg = np.linspace(0,180, 1000)

#Calculates lift coefficent based on
yValues = Lift_Coefficient(alphaDeg)

#Plot the values
plt.plot(alphaDeg, yValues, color="red")

#Print the values (for debugging reasons)
print("Angle of Attack:", alphaDeg)
print("Lift Coefficient:", yValues)

#Title and Axis Labels
plt.xlabel("Angle of Attack (AoA) - α (degrees)", fontsize=12)
plt.ylabel("Lift Coefficient (CL)", fontsize=12)
plt.title("Angle of Attack Effect on Lift", fontsize=14)

#Define y limits
plt.ylim(-1.2,1.2)

#Create a grid
plt.grid(True, which='both')

#Show the window
plt.show()