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
print(og_graph)
import random
import time
#generate the correct coordinate
letters = "ABCDE"
rand_index = random.randint(0, 4)
rand_x = letters[rand_index]
rand_y = random.randint(1, 6)
#full coordinate
coordinate = (f"{rand_x}{rand_y}")
print(coordinate)
#counter of lives and keys
game_won = False
lives = 7
key = 0

print("--- The Wolf is Hiding! ---")

#asking user to guess
while lives > 0 and not game_won:
    print(f"\nLives remaining: {lives}")
    guess = input("Enter a coordinate (e.g., A1): ").upper()
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
