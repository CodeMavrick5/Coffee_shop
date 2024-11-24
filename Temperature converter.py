unit=input("Enter what do you what to convert your temperature to? (example: C to K ) choose between celesius and fahrenheit and kelvin (C/F/K)\n").lower()
temp=float(input("Enter the temperature\n"))


if unit=="c to f":
  temp=round((temp *9)/5 +32, 1)
  print(f"the temperature in fahrenheit is: {temp}°F")
  
elif unit=="f to c":
  temp=round((temp-32) *5/9, 1)
  print(f"The temperature in celesius is: {temp}°C") 
  
elif unit=="k to c":
   temp = temp - 273
   print(f"The temperature in celesius is: {temp}°C") 
   
elif unit =="c to k":
   temp = temp+273
   print(f"The temperature in kelvin is: {temp}k") 
   
elif unit =="f to k":
   temp=round((temp-32) *5/9, 1)
   temp = temp + 273
   print(f"The temperature in kelvin is: {temp}k") 
   
elif unit=="k to f":
   temp = temp - 273
   temp=round((temp *9)/5 +32, 1)
   print(f"the temperature in fahrenheit is: {temp}°F")
    
else:
  print(f"The {unit} you have put in is invald")