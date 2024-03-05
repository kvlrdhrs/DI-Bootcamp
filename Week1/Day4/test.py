
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich",
                   'Chicken sandwich', "Pastrami sandwich"]

# Remove all occurrences of "Pastrami sandwich"
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Prepare the orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.lower()}")

# Print a message listing each sandwich that was made
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich)