def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error!"

print("1.Add 2.Sub 3.Mult 4.Div")
choice = input("Enter (1/2/3/4): ")
n1 = float(input("First number: "))
n2 = float(input("Second number: "))

if choice == '1': print("Result:", add(n1, n2))
elif choice == '2': print("Result:", subtract(n1, n2))
elif choice == '3': print("Result:", multiply(n1, n2))
elif choice == '4': print("Result:", divide(n1, n2))
else: print("Invalid")

