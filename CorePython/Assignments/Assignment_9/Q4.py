# Write a program to find sum of n numbers using recursion.

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
    
n=int(input("Enter number:"))
print(f'Sum of  first {n} numbers using recursive function is {sum(n)}')