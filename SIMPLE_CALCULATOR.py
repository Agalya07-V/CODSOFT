a = float(input("Enter the first value: "))
b = float(input("Enter the second value: "))
print("Which operator do you want?")
print("If you want addition, enter 1")
print("If you want subtraction, enter 2")
print("If you want multiplication, enter 3")
print("If you want division, enter 4")
choice = int(input("Enter your choice: "))

if choice == 1:
    c = a + b
    print("The addition of two values =", c)
elif choice == 2:
    c = a - b
    print("The subtraction of two values =", c)
elif choice == 3:
    c = a * b
    print("The multiplication of two values =", c)
elif choice == 4:
    if b != 0:
        c = a / b
        print("The division of two values =", c)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice")