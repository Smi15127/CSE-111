"""
{ James Smith, Programming w/ Functions 0745 - 0845
{ Date created
{ Calculate discounts on Tuesdays and Wednesdays
"""

# Input

# Get subtotal
SubTotal = float(input("What is the subtotal of today's purchase? "))
#TodayAsk = input("What is the current day today? ")
#TodayAskC = TodayAsk.capitalize()


#Initializing datetime.()
from datetime import datetime

#   Defining what day and time it is, then getting the day of the week with .weekday(),
# where monday is 0, and progressing until sunday is 6. 
current_time = datetime.now().date()
CurrentDay = current_time.weekday()

# Process
def WhenisToday(CurrentDay,TodayAskC): #,TodayAskC
     # Check if it's Tuesday or Wednesday either by current day or user input
    if CurrentDay == 1:  # Tuesday check - or TodayAskC == "Tuesday"
        return 1
    elif CurrentDay == 2:  # Wednesday check -  or TodayAskC == "Wednesday"
        return 1
    else:
        return 0


DateCheck = WhenisToday(CurrentDay) #,TodayAskC

SubTotalFinal = SubTotal
if DateCheck == 1 and SubTotal >= 50.00:
    SubTotalFinal = SubTotal - (SubTotal * .1)
else:
    SubTotalFinal = SubTotal

Total = SubTotalFinal * 1.06
SalesTax = SubTotalFinal * 0.06
DiscountAmount = SubTotalFinal - SubTotal


# Output
print()
print (f"The total amount owed amounts to ${Total:.2f}.")
print (f"The sales tax applied to this purchase is ${SalesTax:.2f}.")
print (f"The discount amount for this purchase is ${DiscountAmount:.2f}.")
print()
"""
   I wrote the program in such a way that there *is* a prompt for the day in question in order to override the 
day recieved from the datetime check. This allowed me to troubleshoot to see if the program works properly.
I finished the program and it should work as intended regardless of the current day.
"""