#Metro qr ticket booking
import json
import math
import qrcode                                             #MODULES
from IPython.display import Image
import random
import matplotlib.pyplot as plt
class metro:
    a="|||*   *   *   *   *   *   *|||<<< METRO BOOKING  >>>||| *   *   *   *   *   *   *|||"

    #def _init_(self,username,password,phoneno,email):                                   #class
       # self.username=username
        #self.password=password
        #self.phoneno=phoneno
        #self.email=email
    def register(self,username,password,phoneno,email):                                    #register method
        file=[{"username":username,
              "password":password,
              "phone number":phoneno,
              "email":email
              }]
        with open("user_details.json","w") as f:                                         #json file to store user data
            json.dump(file,f,indent=8)
        print('----------------------------------------------<<<   REGISTER SUCCESS   >>>------------------------------------------------')
    def login(self,username,password):                                                #login method
        with open("user_details.json","r") as f:                                      #json file to get user data
            data=json.load(f)
        if(data[0]["username"]==username and data[0]["password"]==password):          #password validation
            print("------------------------------------------<<<   LOGIN SUCCESS   >>>---------------------------------------------------")
            return True
        else:
            print()
            print("\t")
            print("ERROR: -->> Invalid credentials\n --->>>  Please enter correct details")
            return False
    def journey(self,source,destination):                                     #journey method
        self.source=source
        self.destination=destination
        a=["JBS parade ground","Secunderabad West","Gandhi hospital","Musheerabad","RTC Cross roads","Chikkadpalli","Narayanaguda","Sultan Bazaar","MGBS"]
        with open("metro_stations.json","w") as f:              #storing station names in json file
              json.dump(a,f,indent=8) 
        with open("metro_stations.json","r") as f:              #getting station names to a variable
             station_getter=json.load(f)
        #print(station_getter)
        if self.source==self.destination:                       
            return False
        print(f"-------> Your pickup point is \"{station_getter[self.source-1]}\"\n")
        print(f"-------> Your Destination point is \"{station_getter[self.destination-1]}\"\n")
    def get_fare(self,source,destination,fare_amount=0,):          #fare method
        with open("metro_stations.json","r") as f:
            stations=json.load(f)
        no_of_stations=int(math.fabs(source-destination)+1)          #calculating no of stations
        #print(no_of_stations)
        fare_amount=float((no_of_stations)*5)                        #calculating total amount
        
        print(f"---->>>  No of stations:{no_of_stations}")
        print(f"---->>>  Fare amount is Rs.{fare_amount}")
    def book_ticket(self,source,destination):                           #book ticket method
        self.source=source
        self.destination=destination
        with open("metro_stations.json","r") as f:                                   #qrcode generation
            stations=json.load(f)
        data=f"This Ticket is valid between {stations[self.source-1]} and {stations[self.destination-1]}"
        qr=qrcode.make(data)
        #qr.show()
        #qr.save("xz.png")                                   #showing qr code in console using matplotlib by adjusting wid,height
        qr.show()
        f=plt.figure()
        f.set_figheight(2)
        f.set_figwidth(2)
        plt.imshow(qr,cmap="gray")
        print("---->>>>  your ticket number is",random.randint(100000000,999999999))      #ticket number
        print("|||*   *   *   *   *   *   *|||<<< THANK YOU  >>>||| *   *   *   *   *   *   *|||")

def conti():                          #continue method
    cont=int(input("  Do you want to login or exit\n   [1]--->>  LOGIN\n   [2]--->>  EXIT     "))
    if cont==1:
        return True
    else:
        return False
            
print(metro.a)
while True:
    choice=int(input("Select\n   [1]--->> REGISTER\n   [2]--->> LOGIN\n   [3]--->>  EXIT\n"))  #user choice
    if choice==1:
        user_name=input("->Enter unique username: ")
        pass_word=input("->Enter password: ")              #asking user to enter data for registering
        phone_number=int(input("->Enter phone number: "))
        email=input("->Enter your email: ")
        m1=metro()
        m1.register(user_name,pass_word,phone_number,email)
        n= conti()
        if n==True:
            continue
        else:
            break
    elif choice==2:
        user_name=input("->Enter username: ")                #user login details
        pass_word=input("->Enter password: ")
        m1=metro()
        ne= m1.login(user_name,pass_word)
        if ne==True:
            break
        else:
            continue
    elif choice==3:
        print("Thank you")                           #exit
        break                              
    else:
        print("please,enter correct choice")       #wrong choice
print()
print()
print("1-->>  JBS parade ground\n2-->>  Secunderabad West\n3-->>  Gandhi hospital\n4-->>  Musheerabad\n5-->>  RTC Cross roads\n6-->>  Chikkadpalli\n7-->>  Narayanaguda\n8-->>  Sultan Bazaar\n9-->>  MGBS")
print()                           #pickup
print()
source=int(input("Enter Pickup point[1-9]:-->> "))
print()
print()
print("1-->>  JBS parade ground\n2-->>  Secunderabad West\n3-->>  Gandhi hospital\n4-->>  Musheerabad\n5-->>  RTC Cross roads\n6-->>  Chikkadpalli\n7-->>  Narayanaguda\n8-->>  Sultan Bazaar\n9-->>  MGBS")
destination=int(input("Enter destination point[1-9]:-->> ")) #destination
print()
station=m1.journey(source,destination)
if station==False:              #checking source and destination are same or not
    print("pickup point and destinations are same,hence you cannot book the ticket")
m1.get_fare(source,destination)
booking=int(input("do you want to book ticket?\n[1].YES\n[2].NO\n"))    #asking user for booking
if booking==1:
    m1=metro()
    m1.book_ticket(source,destination)
else:
    exit()





#Spam messages 
# import random
# import pyautogui as pg
# import time
# animal=('monkey','donkey')
# time.sleep(8)
# for i in range(50):
#     a=random.choice(animal)
#     pg.write("you are a "+a)
#     pg.press('enter') 