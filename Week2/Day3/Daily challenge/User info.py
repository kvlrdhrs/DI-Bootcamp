# Function to get user input
get_input = lambda: (input("Name: "), int(input("Age: ")), int(input("Score: ")))

# Get inputs from the user 5 times
data = [get_input() for _ in range(5)]

# Sort the list by Name > Age > Score
sorted_data = sorted(data, key=lambda x: (x[0], x[1], x[2]))

print(sorted_data)