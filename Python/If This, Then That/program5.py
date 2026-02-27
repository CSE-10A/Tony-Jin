# WAP to check using the sides of a triangle to tell if it is an equilateral triangle or not.

side1 = float(input("Enter the length of the first side: ")) # first side
side2 = float(input("Enter the length of the second side: ")) # second side
side3 = float(input("Enter the length of the third side: ")) # third side
if side1 == side2 == side3: # check if all sides are equal, then print consequent result
    print("The triangle is an equilateral triangle.")
else:
    print("The triangle is not an equilateral triangle.")
