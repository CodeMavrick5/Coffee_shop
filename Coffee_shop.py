print("welcome to Martin's coffee shop\n")

name =input("what is your name\n")

if name== "Martin":
  print("welcome Martin you are the owner of this shop everything for you is for free")
else:
 print("\nHello " +name+ " welcome to our coffee shop " )

menu= "black coffee,latte,espresso,ice coffee"


order=input("\n\nwhat would you like to order here is what we are serving today\n" +menu+ "\n")

if order== "ice coffee":
   price = 9
elif order =="espresso":
    price =7
elif order =="black coffee":
    price =3
elif order =="latte":
    cream= input("Do you want whipped cream?\n")
    if cream == "yes" :
    	price = 8
    else : price = 5
else : 
 print ("sorry we don't have that here")
 exit()
 
 
quantity=input("how many do you want?\n")


total= price* int(quantity)

if name=="Martin":
  print("okay the "+quantity+" " +order+" will be for free and will be ready in just a moment")
  
else:
 print("sounds good " +name+ " the total will be "+str(total)+"EGP and we will have your " + quantity+" "+order + " ready for you  in just a moment")
