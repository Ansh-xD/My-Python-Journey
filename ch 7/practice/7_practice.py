#  *
# ***
#*****

# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(" " * ( n - i ), end="")
#     print("*" * (2 * i - i)), end="")


n = int(input("Enter a number: "))
# Loop through each row
for i in range(1, n+1):
    # Print spaces before stars
    print(' ' * (n - i), end='')
    
    # Print stars (2*i - 1 gives odd number of stars)
    print('*' * (2 * i - 1))
