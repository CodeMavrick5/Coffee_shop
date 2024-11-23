unit=input("Is you temperature in celesius or in fahrenheit? (C/F)\n").lower()
temp=float(input("Enter the temperature\n"))


if unit=="c":
  temp=round((temp *9)/5 +32, 1)
  print(f"the temperature in fahrenheit is: {temp}°F")
elif unit=="f":
  temp=round((temp-32) *5/9, 1)
  print(f"The temperature in celesius is: {temp}°C")
else:
  print(f"The {unit} you have put in is invald")