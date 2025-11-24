import tabulate 
import datetime

def signup():
    u= input("Enter Username: ")
    p= input("Enter Password: ")
    p1= input("Confirm Password: ")
    if p==p1:
        dictionary[u]=p
        print("You have successfully created an account.")
    else:
        print("Confirmed password is incorrect. try again")

def login():
    username = input("Enter your username: ")  
    password = input("Enter your password: ")  
      
    if username in dictionary and dictionary[username] == password:  
        print("Login successful!")  
        print("*****************************************")
    else:  
        print("Invalid username or password. Please try again.")


def building_cart():

    print("You Selected",items[order-1])
    print()
    quant=int(input("How many units do you wish to purchase?  \n"))
    if items[order-1] in shopping_cart:
        print("Repeated Selection")
        idx=shopping_cart.index(items[order-1])
        print(idx)
        shopping_quant[idx]=shopping_quant[idx]+quant        
    else:
        print('New Selection')
        x=shopping_cart.append(items[order-1])
        y=shopping_quant.append(quant)
        z=value.append(price[order-1]) 


def billing():
    print()
    print('Shopping is complete, Displaying Shopping Cart')
    print()
    a=input("Enter your Address:-")
    print("*****************************************************************************")
    print("*****************************************************************************")
    print()
    print('ITEM','QUANT','UNIT PRICE','TOTAL',sep='\t\t')
    print(tabulate.tabulate([]))
   
   
    gt=0

    for k in range(len(shopping_cart)):
        idx=items.index(shopping_cart[k])
        unit_price=price[idx]
        tp=shopping_quant[k]*value[k]
        gt+=tp
        print(shopping_cart[k],shopping_quant[k],unit_price,tp,sep='\t\t')

    print()

    print('The total amount is',round(gt, 2))
    print()
    print("Total amount to be paid after 18% GST is",gt*18/100)
    print()
    print("Your order will be delievered to",a)
    print()
    print("For any query Contact us on:-1234567890")
    print()
    print("If you wish to apply order cancellation please visit www.cherryapplestore.com. Your funds will be returned before 48 hours.")
    print()
    print("************************************************************************************************")
    print("Thank your for Visiting!!")
    print()
    print("Come Again Soon!!")



print("--------------:WELCOME TO APPLE STORE:--------------")
print("HELLO!!")
print("I AM CHERRY")
n=input("May I Know Your Name:-")
print()
print("Nice To Meet U",n)                           
dictionary=dict()
while True:
    print("*******************************")
    print("1. SIGNUP")
    print("2. LOGIN, already an existing user")
    x=int(input("How would you like to proceed further?"))
    if x==1:
        signup()
        print("Now Login To Continue")
    elif x==2:
        login()
        break    



x=datetime.datetime.today()
print("Today's Date and Time is:----",x,"----")

print()

print ("welcome to the main menu:-")
items=('IPHONE','  IPAD  ','MACBOOK',' WATCH','  IOS ','  TV  ')
price=(123000,100000,180000,73000,110000,250000)
print(tabulate.tabulate([price],headers=['1.IPHONE','2.IPAD','3.MACBOOK','4.WATCH','5.IOS','6.TV'],tablefmt="fancy_grid"))
shopping_complete=0

print()
shopping_cart=[] 
shopping_quant=[]
value=[]


while True:    
      order=int(input('enter 1 to 6 to select an apple store item,7 to proceed to checkout\n'))
      if order <=6:
        building_cart()
      else:
          print('proceeding to checkout')
          break
shopping_complete=1


billing()





               
          