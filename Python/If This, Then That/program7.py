"""""
WAP to convert temperatures to and from Celsius and Fahrenheit.

[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

Expected Output :

60°C is 140 in Fahrenheit
45°F is 7 in Celsius
"""

ctof = float(input("Enter temperature in Celsius: ")) # c to f variable
ftoc = float(input("Enter temperature in Farenheit: ")) # f to c variable
print(str(ctof) + "°C is " + str((ctof * 9/5) + 32) + " in Fahrenheit") # convert c to f using formula and print result
print(str(ftoc) + "°F is " + str((ftoc - 32) * 5/9) + " in Celsius") # convert f to c using formula and print result
