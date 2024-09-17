# Get the number for which to print the table
number = int(input("Enter the number for which you want to print the multiplication table: "))

# Print the table header
print(f"\nMultiplication Table for {number}:\n")
print("Multiplication Table:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
