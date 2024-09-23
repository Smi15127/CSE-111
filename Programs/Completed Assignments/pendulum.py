"""
{ James Smith, Programming w/ funtions 0745 - 0845
{ Week of 16 SEPT 24
{ Purpose of code
"""
import math
#input
PendLength = int(input("What is the length of your pendulum in meters? "))

#Process
SwingTime = float(math.sqrt(PendLength / 9.81) * (2 * math.pi)) 

#Output

print (f"The swingtime of your pendulum that is {PendLength} meters long is {SwingTime:.2f} seconds.")

"""
Conclusion section
"""