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
letters = "ABCDEF"
rand_index = random.randint(0, 5)
rand_x = letters[rand_index]
rand_y = random.randint(1, 6)
#full coordinate
coordinate = (f"{rand_x}{rand_y}")
print(coordinate)

#counter of lives
lives = 10
#asking user to guess
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
elif guess != 
                                                                                
                                                                                
                                                                                
                                                                                
