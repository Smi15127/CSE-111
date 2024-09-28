"""
{ James Smith, Programming w/ Functions 0745 - 0845
{ Week of 22 SEPT 24
{ Calculate the volume of space inside a tire
"""
import math
import csv

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

#Initializing datetime.()
from datetime import datetime

#   Defining what day and time it is in order to append
current_date = datetime.now().date()

TireVolume = round(float((math.pi * (mmWidth ** 2) * AspectRatio * (mmWidth * AspectRatio + 2540 * Diameter)) / 10000000000), 2)

new_data = [current_date, mmWidth, AspectRatio, Diameter, TireVolume]

# The filepath of the csv file
file = 'c:\\Users\\it_is\\Documents\\School\\Fall 2024\\CSE 111\\Programs\\Volumes.txt' 

print("Now opening Volumes.txt") # Lets the user know the file is being opened.
print()

try:
    with open(file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)

        # This argument will attempt to skip the header if present, which it will be.
        try:
            next(csvreader)  # Skip header row if present
        
        except StopIteration:
        # Action in the case that the file is empty
            pass


        data = list(csvreader)
        if len(data) == 0:
            print ("There is no data currently present in this file.")
        else:
            print("Existing data in file:")
            # The for loop ensures the file loops through all available rows.
            for row in data:
                current_date, mmWidth, AspectRatio, Diameter, TireVolume = row
                print(row)

except FileNotFoundError:
    # File doesn't exist yet
    print(f"The file {file} does not exist. It is now created.")


print()
print("Would you like to append the new information to the file?")
choice = input("If yes, enter yes. If no, enter no: ")
choice = choice.capitalize()
print()

if choice == 'Yes':
    with open(file, 'a', newline='') as csvfile:
        # New is being written to the file
        writer = csv.writer(csvfile)
        writer.writerow(new_data)
        print ("Data on Volumes.txt has been updated.")

    print()
    print("Now closing Volumes.txt")
    csvfile.close()
    print()
elif choice == 'No':
    print("Volumes.txt is now closed, thank you and have a good day.")

else:
    print("Your choice was not valid. Please enter either yes, or no.")

"""
Conclusion section
"""