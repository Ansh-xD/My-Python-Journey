n = int(input("Enter a number: "))

def patterm(n):
    if(n==0):
        return
    print("*" * n)
    patterm(n-1)
    
print(patterm(n))