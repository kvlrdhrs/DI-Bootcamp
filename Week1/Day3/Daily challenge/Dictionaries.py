# Daily Challenge: Dictionaries

# challenge 1
word = input("Enter a word: ")

letter_indexes = {}

for index, letter in enumerate(word):
    # Ensure the letter is a string
    letter = str(letter)

    # If the letter is not already in the dictionary, add it with an empty list as the value
    letter_indexes.setdefault(letter, []).append(index)

# Print the resulting dictionary
print(letter_indexes)

# challenge 2
def items_you_can_afford(items_purchase, wallet):
    # Remove the "$" sign and commas from the wallet amount
    wallet_amount = int(wallet.replace("$", "").replace(",", ""))

    # Create a list to store affordable items
    affordable_items = []

    # Iterate through items and check affordability
    for item, price in sorted(items_purchase.items()):
        item_price = int(price.replace("$", "").replace(",", ""))
        if item_price <= wallet_amount:
            affordable_items.append(item)
            wallet_amount -= item_price  # Reduce wallet amount after purchase

    # Sort and print the list of affordable items
    affordable_items.sort()
    if affordable_items:
        print(affordable_items)
    else:
        print("Nothing")


# Example 1
items_purchase_1 = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet_1 = "$300"
items_you_can_afford(items_purchase_1, wallet_1)

# Example 2
items_purchase_2 = {
    "Apple": "$4",
    "Honey": "$3",
    "Fan": "$14",
    "Bananas": "$4",
    "Pan": "$100",
    "Spoon": "$2"
}

wallet_2 = "$100"
items_you_can_afford(items_purchase_2, wallet_2)

# Example 3
items_purchase_3 = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}

wallet_3 = "$1"
items_you_can_afford(items_purchase_3, wallet_3)