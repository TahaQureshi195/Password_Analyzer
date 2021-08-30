import pyfiglet
import progressbar
import time 
import random


# Function to create 
def animated_marker():
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
# Driver's code
# animated_marker()

result = pyfiglet.figlet_format("Password Analyzer")
print(result)

user_final = input("Enter your password : ")


while(True):
    level = int(input("""How do you want to test your password!,
    For Level 1 : Press 1 - Basic Level
    For Level 2 : Press 2 - Find out your password is in the most common one's in years.
    For Level 3 : Press 3 - Leaked in Breaches ! 
    For Level 4: Press 4 - Extreme scan """))

    if level ==1:
        if len(user_final) < 7:
                print("Password too short ! -- Can Take 0.29 milliseconds crack The Password.")
        elif len(user_final) < 9:
                print("Password weak -- Can Take 5 Hours crack The Password.")
        elif len(user_final) ==10:
                print("Password Fair -- Can Take 5 Day's crack The Password.")
        elif len(user_final) ==11:
                print("Good Password, But Just to be sure use Level 2 incase its one of the common one's.")
        break

    elif level ==2:
        list = [2011,2012 ,2013,2014,2020,2021]
        print("You can detect if your password is one of the most used in years.")
        print(list)
        
        
        with open('p2011.txt','r') as file:   
            for line in file:
                if user_final in line:
                    print("Found in Most common Passwords in year : 2011")

        with open('p2012.txt','r') as file:   
            for line in file:
                if user_final in line:
                    print("Found in Most common Passwords in year : 2012")

        with open('p2013.txt','r') as file:   
            for line in file:
                if user_final in line:                   
                    print("Found in Most common Passwords in year : 2013")

        with open('p2014.txt','r') as file:   
            for line in file:
                if user_final in line:                    
                    print("Found in Most common Passwords in year : 2014")

        with open('p2020.txt','r') as file:   
            for line in file:
                if user_final in line:                    
                    print("Found in Most common Passwords in year : 2020")

        with open('p2021.txt','r') as file:   
            for line in file:
                if user_final in line:                    
                    print("Found in Most common Passwords in year : 2021")
        

    elif level ==3:
        list_common = ['WORDLIST PASSLIST' , 'DavidWittman Wordlist of @1000 Passwords'] 
        print("You can detect if your password is one of the common go to WORDLIST.")
        print(list_common)
        
        
        with open('passlist.txt','r') as file:   
            for line in file:
                if user_final in line: 
                    print("@#$%!"*10) 
                    # animated_marker()
                    print("Password Found In Worlist 1 !! ")  
                

        with open('wordlist.txt','r') as file:   
            for line in file:
                if user_final in line: 
                    print("@#$%!"*10) 
                    # animated_marker()
                    print("Password Found In Worlist 2 !! ") 
        
        
            
                    
    elif level ==4:
        print("Enabling Deep Scan Mode ! ")
        animated_marker()
        print("Here are some basic questions, that will help us in scan. ")
        print("#"*100)
        name = input("Enter your name :")
        birth = int(input("Enter your birthyear:"))
        age = int(input("Enter your age:"))
        pet = input("Enter you pet name:")
        place = input("Where were you born ")
       
        print("#"*100)

        animated_marker()

        if name or age or birth or pet or place   in user_final:
            print("Not more than 2 minutes to hack !")
        sym = ['@' , '!', '#', '$' , '%' , '^','&','*' ,"(",")" , "-"]
        
        if name or age or birth or pet or place not in user_final:
            if sym in user_final:
                if len(user_final) > 12:
                    
                    print("Strong ! ") 