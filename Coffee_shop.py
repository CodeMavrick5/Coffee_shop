print("welcome to Martin's coffee shop\n")

name =input("what is your name\n").lower()

if name== "martin":
  print("welcome Martin you are the owner of this shop everything for you is for free")
else:
 print(f"\nHello {name} welcome to our coffee shop " )

menu= ["black coffee", "latte", "espresso ","ice coffee"]
item1 = menu[0]
item2 = menu[1]
item3 = menu[2]
item4 = menu[3]


order=input("\n\nWhat would you like to order here is what we are serving today\n" "1."+item1+ "\n" "2."+item2+"\n""3."+item3+"\n" "4."+item4+"\n").lower()



if order== "ice coffee" or "4":
   price = 20
   
elif order =="espresso" or "3":
    price =13
    
elif order =="black coffee" or "1":
    price =9
    
if order =="latte" or "2":
   cream= input("Do you want whipped cream?\n")
   if cream == "yes" :
    	price = 14
   else : price = 10
  
else : 
 print ("sorry we don't have that here")
 exit()
 
 
 
quantity=input("how many do you want?\n")


total= price* int(quantity)

if name=="martin":
  print(f"okay the {quantity} {order} will be for free and will be ready in just a moment")
  
else:
 print(f"sounds good  {name} the total will be {total}EGP and we will have your {quantity} {order} ready for you  in just a moment")