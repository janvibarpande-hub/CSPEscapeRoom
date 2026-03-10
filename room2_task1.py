def room2_task1():
    print("Room 2, task 1")
    #setting the random weight
    import random
    rannum = random.uniform(10, 20)
    weight = round(rannum, 1)
    #guess count
    guesses = 3
    #instructions
    input("There are 3 items in the basket: flowers, cookies, and muffins.")
    input("""                                                                                
                                                                                    
                                                                                    
                                                                                    
                                                                                    
                                                                                
                                                                                    
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
    input("A flower weighs 1.1")
    input("A cookie weighs 1.5")
    input("A muffins weighs 2")
    input("You can have 3 total guesses")
    input(f"Calculate the number of each item that is needed for the basket to weigh {weight}.")
    #inventory guess input
    while guesses > 0:
        flower = int(input("How many flowers are needed? ")) * 1.1
        cookie = int(input("How many cookies are needed? ")) * 1.5
        muffin = int(input("How many muffins are needed? ")) * 2
    #guess = weight check
        total = flower + cookie + muffin
        if total != weight:
            guesses -= 1
            input(f"That is incorrect, you have {guesses} attempts left.")
        else:
            print("That is correct!")
            print("You now have a key in your inventory")
        break
    if guesses <= 0:
        print("You lost! Game Over")


room2_task1
