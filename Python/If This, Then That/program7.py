"""""
WAP to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

ctof = float(input("Enter temperature in Celsius: ")) # c to f
ftoc = float(input("Enter temperature in Farenheit: ")) # f to c
print(ctof + "°C" + "is {(ctof * 9/5) + 32} in Fahrenheit") # convert c to f and print result
print(f"{ftoc}°F is {(ftoc - 32) * 5/9} in Celsius") # convert f to c and print result