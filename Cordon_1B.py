#W2D2

#DriftKidErick
# Lab 1B

# Program Prompt/ Purpose: You want to develop a program that gathers the user’s hourly pay (use $14.50), hours worked (32/week), and tax rate for a two-week period. Once you have this information, you want to display the user’s Gross Pay, Uncle Sam’s Share (the amount to be removed for taxes), and the User’s Net Pay. All calcula5ons should be limited to run once, rather than numerous times. Include in your flowchart the use of variables and print statements. Use 20% for the tax rate. 

#Variable Dictionary

hourly = 14.5 #Hourly pay rate

hours = 32  # Hours worked per week

tax = .2    #Tax percentage

biHours= hours * 2 # weekly hours of 32 times 2

grossPay = biHours * hourly #total pay for 2 weeks

taxRemoval = grossPay * tax # amount removed after tax deductions

netPay = grossPay - taxRemoval #Pay after taxes

#Main Code below -------------------------------------------------------------------------

print("       Bi-Weekly Pay Check Calculator")

print()

print("Bi-weekly gross pay: $ {:.2f}".format(grossPay)) #Displays users Gross Pay

print()

print("Bi-weekly Net Pay: $ {:.2f}".format(netPay)) #Displays users Net Pay

print()

print("Uncle Sam's (taxes) bi-weekly take: $ {:.2f}".format(taxRemoval)) #Displays taxes removed from users gross pay

print("-------------------------------------------------") # used as a break from the solution and the final message

print("     User works 32 hours per week and makes 14.50 dollars an hour. \n User's bi-weekly take-home pay is $742.40.")

#End of Main Code--------------------------
