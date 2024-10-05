n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i == 2:
        print('* ' * (n-1))  # Print n-1 stars for the middle row
    else:
        print('* ' * n)  # Print n stars for the first and last row
