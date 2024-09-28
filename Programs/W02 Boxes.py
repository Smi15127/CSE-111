"""
{ James Smith, Programming w/ Functions 0745 - 0845 MW
{ 28 SEPT 24
{ To calculate the number of boxes a company might need in order to make a complete and accurate shipment.
"""
import math
# Input
# Introduces the program
intro = """ Welcome to BoxesCalc. Please enter the total number of items you must package, and how many items you plan
to include inside each box. The boxes this program provides are all assumed to be the same size. 
Please note this program assumes you will not exceed the number you provide for how many items will be included inside 
each box. Please have the maximum number of items that will go in each box noted before requesting calculation, 
or you will be given an incorrect number of boxes with which to complete shipment.
"""
print()
print (intro)
# User prompts for processing information
items = int(input("How many items in total do you need to pack for this shipment? "))
items_per_box = int(input("What is the maximum number of items you plan to include inside each box? "))

# Process
print()
total_boxes = items / items_per_box
total_boxes = math.ceil(total_boxes)

# Output
print(f"The number of boxes that you need in order to complete your shipment is {total_boxes} box(es).")
print()

"""
    This was a very simple program. The hardest part was running a query through chatGPT to see what arguments I needed to
round to the nearest whole number. In this case is was the 'math.ceil' function from the math module.
"""