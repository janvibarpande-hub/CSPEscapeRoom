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
    choice = input("Press ENTER to play again or type 'Q' to quit: ").upper()
    
    if choice == 'Q':
        print("Thanks for playing!")
        break  
