matrix_string = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""

# Step 1: Convert the matrix string into a 2D list
matrix = [list(row) for row in matrix_string.strip().split('\n')]

# Step 2: Initialize an empty list to collect the decoded message
decoded_message = []

# Step 3: Iterate through each column
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        char = matrix[row][col]
        if char.isalpha():
            decoded_message.append(char)
        elif decoded_message and decoded_message[-1].isalpha():
            decoded_message.append(' ')

# Step 4: Join the collected characters to form the final message
# Remove any trailing spaces caused by non-alpha characters at the end
final_message = ''.join(decoded_message).strip()

print(final_message)