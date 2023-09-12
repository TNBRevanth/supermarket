from datetime import datetime
name=input("Enter your Name: ")
# if name.isalpha():
#     print(name)
lists='''

rice-----> Rs 20/- 1kg
sugar----> Rs 50/- 1kg
colgate--> Rs 50/- 1 Piece
salt-----> Rs 25/- 1kg
snickers-->Rs 20/- 1piece
soap------>Rs 30/- 1 Piece
cheese---->Rs 60/- 1 Piece
hair oil-->Rs 110/-1 liter
tomato---->Rs 50/- 1kg
milk------>Rs 28/- 1packet

'''

print(lists)
price=0
pricelist=[]
totalprice=0
finalprice=0
itemlist=[]
qualitylist=[]
pricelist=[]

items={"rice":20,
       "sugar":50,
       "paste":50,
       "salt":25,
       "snickers":20,
       "tomato":50,
       "soap":30,
       "cheese":60,
       "hair oil":110,
       "milk packet":28}
option=int(input("Enter the list of item click '1': "))
if option==1:
    print(lists)
    for i in range(len(items)):
        input1=int(input("if you want to purchase select option 1 or 2 to Exit: "))
        if input1==2:
            break
        elif input1==1:
            item=input("enter your items: ")
            quantity=int(input("Enter your quantity: "))
            if item in items.keys():
                price=quantity*(items[item])
                pricelist.append((items,quantity,items,price))
                totalprice+=price
                itemlist.append(item)
                qualitylist.append(quantity)
                pricelist.append(price)
                gst=(totalprice*5)/100
                finalamount=gst+totalprice
            else:
                print("your items are not available")
        else:
            print("you entered wrong number")
        inp=input("can i bill this item yes or no: ")
        if inp=="yes":
            pass
        if finalamount!=0:
            print(38*"=","supermarket",38*"=")
            print(39*" ","Vijayawada",32*" ")
            print("Name:",name,38*" ","Date&Time:",datetime.now())
            print(90*"-")
            print("s.no",3*"\t ",'item',2*"\t",'quantity',3*"\t",'price')
            for i in range(len(itemlist)):
                print(i,11*" ",11*" ",itemlist[i],11*" ",qualitylist[i],29*" ",price)
            print(70*" ","Total Amount:",totalprice)
            print(70*" ","GST:  ",1*"\t",gst)
            print(90*"-")
            print(70*" ","FinalAmount: ",finalamount)
            print(90*"-")
            print(35*" ","Thanks Please Visit Again")
            print(90*"-")
            print()
        elif inp.lower()=="no":
            pass
        else:
            print("Input given is wrong")
    else:
        print("Please enter the correct item")
        pass
            
