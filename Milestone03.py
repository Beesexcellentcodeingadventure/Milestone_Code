#Ask the user the following:
#The price of an adult's meal (floating point)
#The number of children (integer)
#The number of adults (integer)
#The sales tax rate (floating point)
# The price of a child's meal (floating point)
#The price of an adult's meal (floating point)


adult_number = int(input("How many adults are there?"))
adult_meal = int(input("What is the price of the adult meal?"))

child_number = float(input("How many childern are there?"))
child_meal = float(input("What is the price of the kids's meal?"))

subtotalC = child_number * child_meal
print("The subtotal for childern:", subtotalC)
subtotalA = adult_number * adult_meal
print("The subtotal for adults:", subtotalA)

sales_taxs_rate = float(input("What is the sales tax rate?"))
total = subtotalA + subtotalC * sales_taxs_rate 
print("The total of this meal is:", total)

amount_paid = float(input("What was the amount paid?"))
print("Amount paid:", amount_paid)
change =  amount_paid - total
print("Change:", change)