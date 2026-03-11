""""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of  6 to, 10 print Weird
If n is even and greater than 20, print Not Weird
"""

# note: this code is missing the condition for even numbers below 1 and between 11 and 20, since the problem statement does not specify what to do in those cases.

n = int(input("Enter an integer: ")) # integer variable

if n % 2 != 0: # check if n is divisible by 2
    print("Weird")
elif n >= 2 and n <= 5: # n greater or equal to 2 and less than or equal to 5?
    print("Not Weird")
elif n >= 6 and n <= 10: # n greater or equal to 6 and less than or equal to 10?
    print("Weird")
elif n > 20: # n greater than 20?
    print("Not Weird")