# Creating a list
fruits = ["apple", "banana", "cherry"]

# Printing the list
print("List of fruits:", fruits)
# Creating an empty list
numbers = []

# Adding elements to the list
numbers.append(1)
numbers.append(2)
numbers.append(3)

# Printing the list
print("List after adding elements:", numbers)

# Removing an element from the list
numbers.remove(2)  # Removes the first occurrence of 2
print("List after removing element 2:", numbers)

# Inserting an element at a specific position
numbers.insert(1, 5)  # Inserts 5 at index 1
print("List after inserting 5 at index 1:", numbers)

# Popping an element from the list (removes and returns the last item)
last_element = numbers.pop()
print("List after popping last element:", numbers)
print("Popped element:", last_element)

