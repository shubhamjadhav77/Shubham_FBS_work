# To check number is prime or not
n=int(input("Enter number:"))
for i in range(2,n//2+1):
    if (n%i==0):
        print(f'{n} is not a prime number ')
        break
else:
    print(f'{n} is a prime  number')