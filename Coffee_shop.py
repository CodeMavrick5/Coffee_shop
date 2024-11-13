print("welcome to Martin's coffee shop\n")
name =input("what is your name\n")
print("\nHello " +name+ " welcome to our coffee shop " )
menu= "black coffee,latte,espresso,ice coffee"
order=input("\n\nwhat would you like to order here is what we are serving today\n" +menu+ "\n")
quantity=input("how many do you want?\n")
if order== "ice coffee":
   price = 9
elif order =="espresso":
    price =7
elif order =="latte":
    cream= input("Do you want whipped cream?\n")
    if cream == "yes" :
    	price = 8
    else : price = 5
   
total= price* int(quantity)
print("sounds good " +name+ " the total will be "+str(total)+"EGP and we will have your " + quantity+" "+order + " ready for you  in just a moment")
