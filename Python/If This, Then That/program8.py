""""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of  6 to, 10 print Weird
If n is even and greater than 20, print Not Weird
"""

n = int(input("Enter an integer: "))

if n % 2 != 0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 10:
    print("Weird")
elif n >= 20