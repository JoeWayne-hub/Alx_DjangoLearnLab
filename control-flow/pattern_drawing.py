# Ask the user to enter a number
size = int(input("Enter the size of the pattern: "))

# Set the starting row to 0
row = 0

# Loop through rows using while loop
while row < size:
    # For each row, print stars using a for loop
    for column in range(size):
        print("*", end="")  # Print on the same line
    print()  # Move to the next line after each row
    row += 1  # Go to the next row
