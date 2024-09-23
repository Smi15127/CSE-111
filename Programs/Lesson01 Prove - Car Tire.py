"""
{ James Smith, Programming w/ Functions 0745 - 0845
{ Week of 16 SEPT 24
{ Calculate the volume of space inside a tire
"""
import math

# Input
InputIntro = """
The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters(205). The second number is the aspect ratio(60). 
The third number is the diameter in inches of the wheel that the tire fits.
(15, the R denotes a tire of radial construction)
Use this as reference as you answer the following questions to measure the volume capacity of your tire.
"""
print(InputIntro)
mmWidth = int(input("What is the width of your tire? Please provide in Milimeters: "))
AspectRatio = int(input("What is the aspect ratio of your tire? "))
Diameter = int(input("What is the diameter of your wheel? Please provide in inches: "))

# Process
TireVolume = float((math.pi * (mmWidth ** 2) * AspectRatio * (mmWidth * AspectRatio + 2540 * Diameter)) / 10000000000)

# Output
print (f"The amount of air your tire can hold is approximately {TireVolume:.2f} liters of air.")
print()
"""
Conclusion section
"""