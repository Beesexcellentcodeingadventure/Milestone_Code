#My dad helped me with if and else statements. The rest is me. 

# Meal Price Calculator
# -------------------------------------------------

# 1. Gather core input
child_meal_cost = float(input("What is the price of the child's meal? "))
adult_meal_cost = float(input("What is the price of the adult's meal? "))

child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))

sales_tax_rate = float(input("What is the sales tax rate (please put in decimal form)? "))
sales_tax_decimal = sales_tax_rate / 100

# -------------------------------------------------
# OPTIONAL: Drinks
add_drinks = input("Add drinks? (y/n): ").strip().lower()
if add_drinks == "y":
    drink_price = float(input("  Price per drink: $"))
    drink_qty   = int(input("  Number of drinks: "))
else:
    drink_price = 0.0
    drink_qty   = 0

# OPTIONAL: Appetizers
add_apps = input("Add appetizers? (y/n): ").strip().lower()
if add_apps == "y":
    app_price = float(input("  Price per appetizer: $"))
    app_qty   = int(input("  Number of appetizers: "))
else:
    app_price = 0.0
    app_qty   = 0

# -------------------------------------------------
# 2. Calculate subtotal (core meals + optional items)
subtotal = (
    child_meal_cost * child_number +
    adult_meal_cost * adult_number +
    drink_price * drink_qty +
    app_price * app_qty
)

# 3. Sales tax and total before tip
sales_tax = subtotal * sales_tax_decimal
total_before_tip = subtotal + sales_tax

# OPTIONAL: Tip
add_tip = input("Add a tip? (y/n): ").strip().lower()
if add_tip == "y":
    tip_percent = float(input("  Tip percentage (please put in decimal form): "))
    tip_amount  = total_before_tip * (tip_percent / 100)
else:
    tip_amount = 0.0

total = total_before_tip + tip_amount

# 4. Display results (two‑decimal formatting)
print("\n--- Bill Summary ---")
print(f"Subtotal:          ${subtotal:.2f}")
print(f"Sales Tax:         ${sales_tax:.2f}")
if tip_amount:
    print(f"Tip ({tip_percent:.0f}%):{'':<10}${tip_amount:.2f}")
print(f"Total:             ${total:.2f}")

# 5. Split the bill option 
#service_charge = 10%
split_bill = input("Would you like to split the bill? (y/n): ").strip().lower()
if split_bill == "y":
    while True:
        try:
            split_ways = int(input("How many ways are you splting the bill(up to 4 ways)? "))
            if split_ways in [2, 3, 4]:
                #if split_ways in [4]
                split_amount = total / split_ways
                print(f"Each person should pay: ${split_amount:.2f}")
                break
            else:
                print("Please enter 2, 3, or 4.")
        except ValueError:
            print("Please enter a valid number.")

# 5. Payment and change
amount_paid = float(input("\nWhat is the payment amount? $"))
change = amount_paid - total
print(f"Change:            ${change:.2f}")