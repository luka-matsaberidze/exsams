import random

def creat_account():
   creat_account1 =(input("pls enter your name: "))
   creat_account2 = (input("pls enter your username: "))
   creat_account3 = (input("pls enter your password: "))
   creat_account4 = (input("pls enter your repeat password: "))
   if creat_account3 == creat_account4:
        print("nice joob you have GOA bank account "+creat_account1+" "+creat_account2) 
   else:
        print("incorect password try again")
        return creat_account()






#aq maq depozitis kodi

def deposit(): 
    raodenoba = float(input("enter your deposit: "))

    if raodenoba <0:
        print("Insufficient deposit")
        return 0


    else:
        return raodenoba

#aq maq balancics naxvis kodi

def show_balance():
   print("YOUR BALANC IS "+str(balance)+" lari")



#aq maq gamoyenebuli depositis 

def deposit_to_someone():
   deposit_someone1 = (input("first enter Name of the transferee: "))
   deposit_someone2 = (input("second enter lastName of the transferee: "))
   deposit_someone3 = (input("enter your transferee credit card number: "))
   if len(deposit_someone3) == 16:
    print("its corect!")
   else:
       print("not found try again")
       return deposit_to_someone()
   
   deposit_someone4= float(input("enter your deposit: "))
   if deposit_someone4 <=0:
      print("not enough money")
      return
   elif balance < deposit_someone4:
      print("you dont have enogh money for deposit to someone please try again later")
      return deposit_to_someone()
   sure= print("are you sure?")
   sure1=print("yes")
   sure2=print("no")
   sure3=input("write word: ")
   
   
   if sure3 == "yes":
      print("okey deposit is secsit!")

    
      
    
    
    


   elif sure3 == "no":
      print("DEPOSIT IS DICLAIND!")
      
      

b = random.randint(1000000000000000,9999999999999999)
   

#aq aris credit cartis gaketeba

def creat_credit_card():
    name = str(input("first enter your name: "))
    lastname = str(input("second enter your lastName: "))
    age = int(input("enter your age: "))
    if age<8 and age>=0:
       print("you are not enough age to have card")
       return proces
    elif age< 18 and age >=8:
       print("you are schoole boy :D")
       gmail = input("enter your email: ")
       print("do you want a schoolcard?: ")
       print("yes")
       print("no")
       creat_card =( input("enter your word: "))
       if   creat_card == "yes":
            print(name + " " + lastname + " you have schoolcard there is your card number: "+str(b) )
            return proces
       elif creat_card == "no":
        print("okey than bye <3")
        return proces
    
      

    
    else:
       print("you are adoult")
    gmail = input("enter your email: ")
    print("which card do you want?")
    creat_card= input("paypal, mastercard or visa: ")
    if creat_card == "visa":
        print(name + " " + lastname + " you have visa card there is your card number: "+str(b) )
    elif creat_card =="mastercard":
        print(name + " " + lastname + "  you have mastercard card there is your card number: "+str(b))
    elif creat_card == "paypal":
        print(name + " " + lastname + " you have paypal card there is your card number: "+str(b))


    
    




balance = 0
proces = True


#aq maq gamoyenebuli while ris saxvalebitac sanam momxmarebeli ar aricevs exsits an rame sxva arcevans ar gaaketebs manamde ar gacerdes

while proces:
    print("*************************")
    print("Hello to GOA bank:3")
    print("*************************")
    print("BANK PROGRAM")
    print("*************************")
    print("0.creat account")
    print("1.deposit")
    print("2.deposit to someone")
    print("3.show balance")
    print("4.creat credit card")
    print("5.exsit")
    print("*************************")

    

    choose = input("please enter your choose: ")

    if choose =="0":
       creat_account()
    elif choose =="1":
        balance += deposit()
    elif choose =="2":
        deposit_to_someone()
    elif choose == "3":
        show_balance()
    elif choose =="4":
        creat_credit_card()
    elif choose =="5":
        proces = False
        
        print("thank you have nice day :3")
        
    else:
        
        print("there not is that choose") 