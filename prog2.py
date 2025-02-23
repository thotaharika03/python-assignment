fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "potato"]

#Prices
fruit_prices = {"apple": 1.00, "banana": 0.50, "cherry": 2.00}
vegetable_prices = {"carrot": 0.50, "broccoli": 1.50, "potato": 1.00}

  #Get user input
print("Available fruits:", fruits)
print("Available vegetables:", vegetables)

fruit_wanted = input("Enter the fruit you want to buy (or 'none'): ")
vegetable_wanted = input("Enter the vegetable you want to buy (or 'none'): ")

#Check availability
if fruit_wanted.lower() != "none" and fruit_wanted in fruits:
print(f"{fruit_wanted} is available.")
else:
print(f"{fruit_wanted} is not available.")

if vegetable_wanted.lower() != "none" and vegetable_wanted in vegetables:
print(f"{vegetable_wanted} is available.")
else:
print(f"{vegetable_wanted} is not available.")

#Calculate total cost
total_cost = 0
if fruit_wanted.lower() != "none" and fruit_wanted in fruits:
total_cost += fruit_prices[fruit_wanted]
if vegetable_wanted.lower() != "none" and vegetable_wanted in vegetables:
total_cost += vegetable_prices[vegetable_wanted]

print(f"Total cost: ${total_cost:.2f}")

#Ask if user wants to buy more
buy_more = input("Do you want to buy more? (yes/no): ")
if buy_more.lower() == "yes":
print("You can buy more fruits and vegetables.")
else:
print("Thank you for shopping!")