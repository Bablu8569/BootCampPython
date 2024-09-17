def operator_demo():
    # Arithmetic Operators
    a = 10
    b = 5
    print(f"Arithmetic Operations between {a} and {b}:")
    print(f"a + b = {a + b}")  # Addition
    print(f"a - b = {a - b}")  # Subtraction
    print(f"a * b = {a * b}")  # Multiplication
    print(f"a / b = {a / b}")  # Division
    print(f"a % b = {a % b}")  # Modulus
    print(f"a ** b = {a ** b}")  # Exponentiation
    print(f"a // b = {a // b}")  # Floor Division

    # Comparison Operators
    print("\nComparison Operations:")
    print(f"a == b: {a == b}")  # Equal to
    print(f"a != b: {a != b}")  # Not equal to
    print(f"a > b: {a > b}")    # Greater than
    print(f"a < b: {a < b}")    # Less than
    print(f"a >= b: {a >= b}")  # Greater than or equal to
    print(f"a <= b: {a <= b}")  # Less than or equal to

    # Logical Operators
    x = True
    y = False
    print("\nLogical Operations:")
    print(f"x and y: {x and y}")  # Logical AND
    print(f"x or y: {x or y}")    # Logical OR
    print(f"not x: {not x}")      # Logical NOT

    # Assignment Operators
    c = 10
    c += 5  # Equivalent to c = c + 5
    print(f"\nAfter c += 5, c = {c}")
    c -= 3  # Equivalent to c = c - 3
    print(f"After c -= 3, c = {c}")
    c *= 2  # Equivalent to c = c * 2
    print(f"After c *= 2, c = {c}")
    c /= 4  # Equivalent to c = c / 4
    print(f"After c /= 4, c = {c}")

    # Membership Operators
    my_list = [1, 2, 3, 4, 5]
    print("\nMembership Operations:")
    print(f"3 in my_list: {3 in my_list}")  # Check if 3 is in the list
    print(f"6 not in my_list: {6 not in my_list}")  # Check if 6 is not in the list

    # Identity Operators
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print("\nIdentity Operations:")
    print(f"a is b: {a is b}")  # Check if a and b are the same object
    print(f"a is not c: {a is not c}")  # Check if a and c are not the same object

if __name__ == "__main__":
    operator_demo()
