# WAP to print the day based on the number input. (For example: if input = 1, output = Monday)

num = int(input("Enter a number between 1 and 7: ")) # define variable
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # list of days
print(days[num - 1]) # print day based on input, subtract 1 to account for indexing that starts at 0
