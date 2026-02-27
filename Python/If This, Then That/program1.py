# WAP to check if a single character is a vowel or not.

character = input("Enter a single character: ") # character variable
if character in "aeiouAEIOU": # checks if character is in string of vowels, print consequent result
    print("The character is a vowel.") 
else:
    print("The input is not a single vowel.") 