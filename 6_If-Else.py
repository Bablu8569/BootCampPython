def check_number():
    # Prompt user for input
    number = int(input("Enter a number: "))
    
    # Check if the number is positive, negative, or zero
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

if __name__ == "__main__":
    check_number()

