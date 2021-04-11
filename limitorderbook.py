import datetime;
def marketorder():#function for placing market order
    print("You have selected MARKET order")
    otype=int(input("Enter 1 to BUY and 2 to SELL "))
    if otype==1:
        print('You have selected BUY')
        quantity=int(input("Enter Quantity "))
        ct = datetime.datetime.now()
        print("You have Placed BUY MARKET Order for HDFC Ltd. for "+str(quantity)+" qantity at", ct)
    elif otype==2:
        print('You have selected SELL')
        quantity=int(input("Enter Quantity "))
        ct = datetime.datetime.now()
        print("You have Placed SELL Market Order for HDFC Ltd. for "+str(quantity)+" qantity at", ct)        
    elif otype !="":
        print('Not Valid Choice Try again')
        exit();
def limitorder(): #function for placing limitorder
    print("You have selected LIMIT Order")
    otype=int(input("Enter 1 to BUY and 2 to SELL"))
    if otype==1:
        print('You have selected BUY')
        price=float(input("Enter Price at which you want to buy(Should be between Upper Circuit and lower circuit "))
        quantity=int(input("Enter Quantity "))
        ct = datetime.datetime.now()
        print("You have Placed BUY LIMIT Order for HDFC Ltd. at"+str(price)+" for "+str(quantity)+" qantity at", ct)
        margin=price*quantity;
        print("Margin amount blocked is Rs.",margin)
    elif otype==2:
        print('You have selected SELL')
        price=float(input("Enter Price at which you want to buy(Should be between Upper Circuit and lower circuit "))
        quantity=int(input("Enter Quantity "))
        ct = datetime.datetime.now()
        print("You have Placed SELL Market Order for HDFC Ltd. at"+str(price)+" for "+str(quantity)+" qantity at", ct)
        margin=price*quantity;
        print("Margin amount blocked is Rs.",margin)
    elif otype !="":
        print('Not Valid Choice Try again')
        exit();
def SLorder(): #function for SL orders
    print("You have slected SL order")
    otype=int(input("Enter 1 to BUY and 2 to SELL"))
    if otype==1:
        print('You have selected BUY')
        price=float(input("Enter Price at which you want to buy(Should be between Upper Circuit and lower circuit "))
        quantity=int(input("Enter Quantity "))
        trigger=float(input("Enter Trigger Price"));
        ct = datetime.datetime.now()
        print("You have Placed BUY SL Order for HDFC Ltd. at"+str(price)+" for "+str(quantity)+"trigger price"+str(trigger)+" qantity at", ct)
        margin=price*quantity;
        print("Margin amount blocked is Rs.",margin)
    elif otype==2:
        print('You have selected SELL')
        price=float(input("Enter Price at which you want to buy(Should be between Upper Circuit and lower circuit "))
        quantity=int(input("Enter Quantity "))
        trigger=float(input("Enter Trigger Price"));
        ct = datetime.datetime.now()
        print("You have Placed SELL SL Order for HDFC Ltd. at"+str(price)+" for "+str(quantity)+"trigger price"+str(trigger)+" qantity at", ct)
        margin=price*quantity;
        print("Margin amount blocked is Rs.",margin)
    elif otype !="":
        print('Not Valid Choice Try again')
        exit();
    
print("Welcome")
print("Currently you can trade in HDFC Ltd. (NSE:HDFC)")
print("Please Select from follwing options to trade")
print("Select 1 for MARKET Order")
print("Select 2 for LIMIT Order")
print("Select 3 for SL Order")
toption=int(input("Enter option"))
if toption==1:
    marketorder();
elif toption==2:
    limitorder();
elif toption==3:
    SLorder();
elif toption !="":
    print("Not Valid Choice Try again")
    exit();