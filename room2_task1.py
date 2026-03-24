def room2_task1():
    print("Room 2, task 1")
    #importing
    import time
    import random
    #setting the random weight
    rannum = random.uniform(10, 20)
    weight = round(rannum, 1)
    #guess count
    guesses = 3
    #instructions
    print("There are 3 items in the basket: flowers, cookies, and muffins.")
    time.sleep(3.0)
    print("""                                                                                
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                
                                                                                    
                                   _______________________                          
                                 _|≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡|_                        
                               _|-=|                     |--|_                      
                              /_-/                         \=-\                     
                             │-=│                           │-_│                    
                             │=_│                           │=-│                    
                             │=-│                           │_=│                    
                            \_-_=\_________________________/-=__/                   
                             \-==_-=-_=_-_=_-=-_-_=--_=_-_-=_-_/                    
                              \_=_-_==-_ _=__-=-_-_= =_-_=-_=-/                     
                               \-=_-_==_-=_-=_=_--_=-_=__-=_=/                      
                                \-=--_=-_=_-=--_=_--=-__-=_=/                       
                                 \=_=-__-==_=-_=_=-_-==_=__/                        
                                  \_=-_-_==-_=-__=_-=_-_=-/                         
                                   \-=-_=_-_-=___--==-__-/                          
                                    ≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡                           
                                                                                    
                                                                                """)
    time.sleep(3.0)
    print("A flower weighs 1.1")
    time.sleep(2.5)
    print("A cookie weighs 1.5")
    time.sleep(2.5)
    print("A muffin weighs 2")
    time.sleep(2.5)
    print("You can have 3 total guesses")
    time.sleep(2.5)
    print(f"Calculate the number of each item that is needed for the basket to weigh {weight}.")
    time.sleep(3.5)
    #inventory guess input
    while guesses > 0:
        #flower
        flower = -1
        flower_str = input("How many flowers are needed? ")
        flower_dig = flower_str.isdigit()
        if flower_dig == True:
            flower = int(flower_str) * 1.1
        while flower_dig == False or flower <= -1:
            print("That is not a positive number")
            flower_str = input("How many flowers are needed? ")
            flower_dig = flower_str.isdigit()
            if flower_dig == True:
                flower = int(flower_str) * 1.1
        
        #cookie
        cookie = -1
        cookie_str = input("How many cookies are needed? ")
        cookie_dig = cookie_str.isdigit()
        if cookie_dig == True:
            cookie = int(cookie_str) * 1.5
        while cookie_dig == False or cookie <= -1:
            print("That is not a positive number")
            cookie_str = input("How many cookies are needed? ")
            cookie_dig = cookie_str.isdigit()
            if cookie_dig == True:
                cookie = int(cookie_str) * 1.5
        #muffin
        muffin = -1
        muffin_str = input("How many muffins are needed? ")
        muffin_dig = muffin_str.isdigit()
        if muffin_dig == True:
            muffin = int(muffin_str) * 2
        while muffin_dig == False or muffin <= -1:
            print("That is not a positive number")
            muffin_str = input("How many muffins are needed? ")
            muffin_dig = muffin_str.isdigit()
            if muffin_dig == True:
                muffin = int(muffin_str) * 2
        
    #guess = weight check
        total = flower + cookie + muffin
        if total != weight:
            guesses -= 1
            print(f"That is incorrect, you have {guesses} attempts left.")
        else:
            print("That is correct!")
            print("You now have a key in your inventory")
            break
    if guesses <= 0:
        print("You lost! Game Over")


room2_task1()

                                                                                                    
                                                                                                    
                                                                                                    
                                    \                                                               
                                     │                                                              
                                     /                        \                                     
                                     \                        /                                     
                                \     \                      /     /                                
                                 \     \/──────────────────\/     /                                 
                                  \    /                    \    /                                  
                                   \  /                      \  /                                   
                                    \/                        \/                                    
                                    │                          │                                    
                                    │                          │                                    
                                    │     /────\    /────\     │                                    
                                    │     │    │    │    │     │                                    
                                     │    │    │    │    │    │                                     
                                     │    \────/    \────/    │                                     
                                     │           /\           │                                     
                                     │          /  \          │                                     
                                      │         \──/         │                                      
                                      │\                    /│                                      
                                      │ \__________________/ │                                      
                                       \ │ │  │           │ /                                       
                                        \ \│  │          / /                                        
                                         \ ────────────── /                                         
                                          ----------------                                          
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
