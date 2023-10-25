try:
    x = int(input("What's x? "))
except ValueError:
    print("It's not integer")

print(f"x is {x}")
