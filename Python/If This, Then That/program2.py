# WAP to check if a number is even or odd, where the number is taken as input. (Hint: What is the difference between an even and an odd number?)

num = int(input("Enter a number: ")) # define variable
if num % 2 == 0: # check if number is divisible by 2, then prints consequent result
    print("The number is even.") 
else: 
    print("The number is odd.")