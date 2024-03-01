'''Simulate a billing scenario in a store with two dictionaries 'stock' and 'price'. 
'Stock' contains the items in the store with count. 
'Price' has the price of each item. 
The items that are available in the stock should be displayed to the user. 
User can buy any set of items from the stock. 
After purchase total bill of all items bought should be displayed with remaining stock items. '''
print("\n**************Z Mart**************\n")
stock={"A":20, "B":25, "C":12, "D":34, "E":15, "F":30}
price={"A":999, "B":799, "C":2599, "D":1899, "E":589, "F":2399}
print("Check out our Store")
for k,v in stock.items():
    print(k,v,price[k])
cart={}
while (True):
    item=input("Add item: ")
    if (item in cart):
        cart[item]+=1
    else:
        cart[item]=1
    stock[item]-=1
    c=input("do you want to add more items (y/n)")
    if (c=="n"):
        break
print("\n***Your Cart Summary and Sum Amount***")
total=0
for k,v in cart.items():
    print(k,v)
    total=total+(v*price[k])
print("Your Sum amount is: ",total )
print("\nStock left is :")
for k,v in stock.items():
    print (k,v)
