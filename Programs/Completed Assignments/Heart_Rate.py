"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

Age = int(input("What is your age? "))

MHR = int(220 - Age)

HTR = int(MHR * .85)
LTR = int(MHR * .65)

Output = f"""   With your age at {Age}, your maximum heart rate is {MHR}, and you should strive for a target
heart rate range of {LTR} and {HTR}."""

print (Output)


