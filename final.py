import time
narrator = ["""Oh, look who’s decided to take the scenic route. How... brave of you.
Welcome, dear traveler, to the woods. It’s a lovely day for a walk to Granny’s house, isn't it?
Just you, your little red hood, and a forest full of things that haven't had breakfast yet.
""",
"""Be warned: this path is not for the faint of heart.
To survive the journey, you must prove your worth through a series of trials.
In each stage of your trek, you will face two distinct challenges.
Only by successfully completing these tasks will you earn the keys necessary to unlock the way forward
""",
"""But do not grow complacent. The forest is unforgiving;
a single lapse in judgment or a failed task will strip you of your progress, forcing you to return to the start of the room to try again.
Precision is your only friend here, as you must collect every key to truly escape the narrative.
""",
"""The stage is set. The wolf has already tucked his napkin into his collar.
The only question left is: are you the master of this story, or just the main course?
Do try to keep your wits about you.
It would be such a shame to have to start all the way back at the beginning... again.
"""]
#for how many different phrases there are
para_count = len(narrator)
#print with time lag btwn
for s in range(para_count):
    print(narrator[s])
    time.sleep(5.0)


while True:
    og_graph = """
                       1      2      3      4      5      6                        
                    ╓─────────────────────────────────────────╖                     
                 A  ║      |      |      |      |      |      ║                     
                    ║      |      |      |      |      |      ║                     
                    ║------+------+------+------+------+------║                     
                 B  ║      |      |      |      |      |      ║                     
                    ║      |      |      |      |      |      ║                     
                    ║------+------+------+------+------+------║                     
                 C  ║      |      |      |      |      |      ║                     
                    ║      |      |      |      |      |      ║                     
                    ║------+------+------+------+------+------║                     
                 D  ║      |      |      |      |      |      ║                     
                    ║      |      |      |      |      |      ║                     
                    ║------+------+------+------+------+------║                     
                 E  ║      |      |      |      |      |      ║                     
                    ║      |      |      |      |      |      ║                     
                    ║      |      |      |      |      |      ║                     
                    ╙─────────────────────────────────────────╜                     
                                                                                    
                                                                 
                    """
    graph_list = list(og_graph)
    import random
    import time
    #graphing function
    def graph_mark(guess):
        row_map = {"A": 3,"B": 6, "C": 9, "D": 12, "E": 15}
        col_map = {'1': 20, '2': 27, '3': 34, '4': 41, '5': 48, '6': 55}
    
        lines = og_graph.split("\n")
        char_count = 0
    
        for i in range(row_map[guess[0]]):
            char_count += len(lines[i]) + 1
        char_count += col_map[guess[1]]
    
        graph_list[char_count] = "X"
    #generate the correct coordinate
    letters = "ABCDE"
    rand_index = random.randint(0, 4)
    rand_x = letters[rand_index]
    rand_y = random.randint(1, 6)
    #full coordinate
    coordinate = (f"{rand_x}{rand_y}")
    
    #counter of lives and keys
    game_won = False
    lives = 7
    key = 0
    
    print("--- The Wolf is Hiding! ---")
    
    #asking user to guess
    while lives > 0 and not game_won:
        print("".join(graph_list))
        time.sleep(1.0)
        print(f"\nLives remaining: {lives}")
        guess = input("Enter a coordinate (e.g., A1): ").upper()
        if len(guess) != 2 or guess[0] not in "ABCDE" or guess[1] not in "123456":
            print("INVALID INPUT! Try again")
            continue
        graph_mark(guess)
        if guess == coordinate:
            print("Correct guess")
            time.sleep(1.0)
            print("Great job player, I guess you are smarter that i thought")
            time.sleep(1.0)
            
            game_won = True
        else:
            lives -= 1
            
            if lives == 0:
                print("Game over... The wolf got away.")
            if lives == 3:
                print("I see you're struggling a bit there.")
                print(f"HINT: The wolf is in column {rand_x}")
            else:
                print("Wrong answer player! Try again.")
    if game_won == True:
        print("""Congradulations player, You have sucsessfully found wolf and recieved a
          key but I wonder what else he has in plan for you""")
        break
    if game_won == False:
        choice = input("Press ENTER to retry or type 'Q' to quit: ").upper()
    
        if choice == 'Q':
            print("Thanks for playing!")
        break





    
while True:
    import random
    import time
    flower_list2 = [
        "Sunflower", "Daffodil", "Marigold", "Petunia", "Begonia", 
        "Geranium", "Hydrangea", "Snapdragon", "Lavender", "Jasmine", 
        "Gardenia", "Hyacinth", "Magnolia", "Hibiscus", "Wisteria", 
        "Honeysuckle", "Bluebell", "Buttercup", "Foxglove", "Primrose", 
        "Dandelion", "Carnation", "Chrysanthemum", "Amaranth", "Columbine", 
        "Clematis", "Cyclamen", "Foxglove", "Gardenia", "Gladiolus", 
        "Heather", "Lobelia", "Morning Glory", "Oleander", "Petunia", 
        "Trillium", "Verbena", "Wallflower", "Anemone", "Camellia"]
    answer2 = random.choice(flower_list2).upper()
    letters2 = list(answer2)
    template2 = ["____"] * len(letters2)
    current_display2 = template2
    wrong_guesses2 = 0
    other_letters2 = []
    print(letters2)
    game_won2 = False

    hangmans2 = [' --------------------',
    ''' 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |
    ----------------+---''',
    '''  -----------+                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |                                 
                    |
    ----------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
         |          |                                                               
         |          |                                                               
         |          |                                                               
         |          |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |          |                                                               
       `.|          |                                                               
         |          |                                                               
         |          |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         |          |                                                               
                    |                                                               
                    |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         x          |                                                               
        /           |                                                               
       /            |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'         |                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         x          |                                                               
        / \         |                                                               
       /   \        |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'      ---|                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |                                                               
         x          |                                                               
        / \         |                                                               
       /   \        |                                                               
     ---------------+---''',
    '''                                                                                
         +----------+                                                               
        ,|.         |                                                               
       (   )        |                                                               
        `-'---------|                                                               
      \  |  /       |                                                               
       `.|.'        |                                                               
         |          |
         x          |                                                               
        / \         |                                                               
       /   \        |                                                               
     ---------------+---''',
    '''---GAME OVER---''']

    def letter_placer(guess2, letters2, template2):
        for i in range(len(letters2)):
            if letters2[i] == guess2.upper():
                template2[i] = letters2[i]
        return template2
    print("\n" + " ".join(template2))
    while wrong_guesses2 < (len(hangmans2) - 1):
        guess2 = input("Guess the letter: ").upper() 
        time.sleep(1.0)
        if guess2 in current_display2 or guess2 in other_letters2:
            print("Already guessed!")
            time.sleep(1.0)
            continue

        if guess2.upper() in answer2.upper():
            current_display2 = letter_placer(guess2, letters2, template2)
            print("\n" + " ".join(current_display2))
            time.sleep(1.0)
            print("Great job player!")
            time.sleep(1.0)

            
            if "____" not in current_display2:
                print(f"Winner! The word was {answer2}")
                time.sleep(1.0)
                game_won2 == True
        else:
            wrong_guesses2 += 1
            other_letters2.append(guess2)
            print("Wrong guess")
            time.sleep(1.0)
            print("\n" + " ".join(current_display2))
            time.sleep(1.0)
            print(hangmans2[wrong_guesses2])
            time.sleep(1.0)
    if game_won2 == True:
        print("""Congradulations player, You have sucsessfully found grannie her flowers""")
    if game_won2 == False:
        choice2 = input("Press ENTER to retry or type 'Q' to quit: ").upper()
    
    if choice2 == 'Q':
        print("Thanks for playing!")
        break




    
while True:
    print("Room 2, task 1")
    #importing
    import time
    import random
    #setting the random weight
    game_won3 == False
    rannum3 = random.uniform(10, 20)
    weight3 = round(rannum3, 1)
    #guess count
    guesses3 = 3
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
    while guesses3 > 0:
        #flower
        flower3 = -1
        flower_str3 = input("How many flowers are needed? ")
        flower_dig3 = flower_str3.isdigit()
        if flower_dig3 == True:
            flower3 = int(flower_str3) * 1.1
        while flower_dig3 == False or flower3 <= -1:
            print("That is not a positive number")
            flower_str3 = input("How many flowers are needed? ")
            flower_dig3 = flower_str3.isdigit()
            if flower_dig3 == True:
                flower3 = int(flower_str3) * 1.1
        
        #cookie
        cookie3 = -1
        cookie_str3 = input("How many cookies are needed? ")
        cookie_dig3 = cookie_str3.isdigit()
        if cookie_dig3 == True:
            cookie3 = int(cookie_str3) * 1.5
        while cookie_dig3 == False or cookie3 <= -1:
            print("That is not a positive number")
            cookie_str3 = input("How many cookies are needed? ")
            cookie_dig3 = cookie_str3.isdigit()
            if cookie_dig3 == True:
                cookie3 = int(cookie_str3) * 1.5
        #muffin
        muffin3 = -1
        muffin_str3 = input("How many muffins are needed? ")
        muffin_dig3 = muffin_str3.isdigit()
        if muffin_dig3 == True:
            muffin3 = int(muffin_str3) * 2
        while muffin_dig3 == False or muffin3 <= -1:
            print("That is not a positive number")
            muffin_str3 = input("How many muffins are needed? ")
            muffin_dig3 = muffin_str3.isdigit()
            if muffin_dig3 == True:
                muffin3 = int(muffin_str3) * 2
        
    #guess = weight check
        total3 = flower3 + cookie3 + muffin3
        if total3 != weight3:
            guesses3 -= 1
            print(f"That is incorrect, you have {guesses} attempts left.")
        else:
            print("That is correct!")
            print("You now have a key in your inventory")
            game_won3 == True
            
    if guesses3 <= 0:
        print("You lost! Game Over")
    if game_won3 == True:
        print("""Congradulations player, You have sucsessfully created the perfect basket""")
    if game_won3 == False:
        choice3 = input("Press ENTER to retry or type 'Q' to quit: ").upper()
    if choice3 == 'Q':
        print("Thanks for playing!")
        break                                    









while True:
    game_won4 = False
    import random
    import time
    phrase_list4 = [
        ["grandmother", "what", "big", "eyes", "you", "have"],
        ["all", "the", "better", "to", "see", "you", "with", "my", "dear"],
        ["grandmother", "what", "big", "ears", "you", "have"],
        ["all", "the", "better", "to", "hear", "you", "with", "my", "dear"],
        ["grandmother", "what", "big", "teeth", "you", "have"],
        ["all", "the", "better", "to", "eat", "you", "with"],
        ["i", "am", "going", "to", "visit", "my", "grandmother"],
        ["she", "lives", "just", "beyond", "those", "trees"],
        ["little", "red", "riding", "hood"],
        ["do", "not", "speak", "to", "any", "strangers", "on", "the", "road"], 
        ["he", "swallowed", "poor", "old", "grandmother"], 
        ["the", "wolf", "had", "a", "very", "good", "appetite"]
        ]


    #scramble
    phrase4 = random.choice(phrase_list4)
    unscram_phr4 = " ".join(phrase4)
    length4 = len(phrase4)
    work_phrase4 = []
    for i in range(length4):
        word4 = phrase4[i]
        #seperate each letter in the word into its own part of the list
        string_list4 = list(word4)
        random.shuffle(string_list4)
        #join the scrambled letters back together
        new_word4 = "".join(string_list4)
        #make sure the word is scrambled properly
        if new_word4 == word4:
            string_list4 = list(word4)
            random.shuffle(string_list4)
            new_word4 = "".join(string_list4)

        work_phrase4.append(new_word4)
        #add the words into a list
        new_phrase4 = " ".join(work_phrase4)

    guess4 = 5
    print("You have arrived at Granny's house but she has a lock on her door.")
    time.sleep(3)
    print("""
                                               
        ══════════════════════════════════     
       ║                                  ║    
       ║  ──────────────────────────────  ║    
       ║ │ EEEE N    N TTTTT EEEE RRRRR │ ║    
       ║∙│ E    NN   N   T   E    R   R │∙║    
       ║ │ E    N N  N   T   E    RRRRR │ ║    
       ║ │ EEEE N  N N   T   EEEE R R   │ ║    
       ║∙│ E    N   NN   T   E    R  R  │∙║    
       ║ │ EEEE N    N   T   EEEE R   R │ ║    
       ║  ──────────────────────────────  ║    
       ║                                  ║    
        ══════════════════════════════════     
                                               
    """)
    time.sleep(3)
    print("To unlock the door you need to unscramble the phrase in 5 or less guesses")
    time.sleep(3)
    print("The phrase is: ")
    time.sleep(3)
    print(new_phrase4)
    time.sleep(3)
    while guess4 > 0:
        unscrambled_up4 = input("Please enter the uncrambled phrase: ")
        unscrambled4 = unscrambled_up4.lower()
        if unscrambled4 == unscram_phr4:
            print("That is correct!")
            print("You have recieved a key")
            game_won4 == True
        else:
            guess4 -= 1
            print(f"That is incorrect, you have {guess4} left")
    if guess4 == 0:
        print("You have run out of guesses")
        print("Game Over!")
    if game_won4 == True:
        print("""Congradulations player, You have sucsessfully created the unscrambled grannies code""")
    if game_won4 == False:
        choice4 = input("Press ENTER to retry or type 'Q' to quit: ").upper()
    if choice4 == 'Q':
        print("Thanks for playing!")
        break


