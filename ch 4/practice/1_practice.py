# Question  -  Write a program to store seven fruits in a list entered by the user



fruits = []

f1 = input("Enter Fruit name: ")
fruits.append(f1)
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)
f5 = input("Enter Fruit name: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)
f7 = input("Enter Fruit name: ")
fruits.append(f7)

print(fruits)



# chat gpt answer


# Initialize an empty list to store the fruit names
fruits = []

# Loop to get 7 fruit names from the user
for i in range(7):
    fruit = input(f"Enter fruit #{i + 1}: ")
    fruits.append(fruit)

# Print the list of fruits
print("\nList of fruits:")
print(fruits)
