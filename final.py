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
    time.sleep(10.0)


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
            print("you recieved your first key")
            time.sleep(1.0)
            print("""                                                                  
                   ,-----.                                                          
                 ,' ,-+-. `.                                                        
                /  / | | \  \                                                       
               (  (  / \  )  )                                                      
                \  \/ + \/  /                                                       
                 `. `---' ,'                                                        
                   '|-|--'                                                          
                    | |                                                             
                    | |                                                             
                    | | _ _                                                         
                    ||_|_|_|                                                        
                    ||_ _                                                           
                    ||_|_|                                                          
                    ||_ _ _                                                         
                    |+_|_|_|                                                        
                    \ |                                                             
                     `|       """)
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
    if game_won == False:
        choice = input("Press ENTER to play again or type 'Q' to quit: ").upper()
    
    if choice == 'Q':
        print("Thanks for playing!")
        break

