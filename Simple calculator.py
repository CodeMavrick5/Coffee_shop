operator=input("select your operator: (+ , - , x , / )\n")
no1=float(input("enter the 1st number: "))
no2=float(input("enter the 2nd number: "))

if operator== "+":
  answer= round(float(no1 + no2), 2)
  print(f"the answer is {answer}")
  
if operator=="-":
  answer=round(float(no1 - no2), 2)
  print(f"the answer is {answer}")
  
if operator=="x":
  answer=round(float(no1 * no2), 2)
  print(f"the answer is {answer}")
  
if operator=="/":
  answer=round(float(no1 / no2), 2)
  print(f"the answer is {answer}")