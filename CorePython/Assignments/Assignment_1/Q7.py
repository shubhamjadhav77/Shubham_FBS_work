
# Program to Find the Roots of a Quadratic Equation

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


D = b**2 - 4*a*c


root1 = (-b + (D)**0.5) / (2*a)
root2 = (-b - (D)**0.5) / (2*a)


print(f"The roots of the equation are: {root1} and {root2}")
