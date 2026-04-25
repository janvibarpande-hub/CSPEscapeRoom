
#Module that creates mazes
from pyamaze import maze, agent

#Used for pauses and the timer
import time

#To manage cocurrent tasks
import threading


time_up = False

#Creating the timer function
def start_timer(seconds):
    global time_up
    time.sleep(seconds)
    time_up = True

#Creating the function that creates the maze
def makemaze():
    global time_up
    time_up = False 

    #Maze size
    m = maze(15, 15)
    m.CreateMaze()

    #automatically opens maze in full screen
    m._win.attributes('-fullscreen', True)
    m._win.bind("<Escape>", lambda e: m._win.destroy())

    #setting up the player
    a = agent(m, filled=True, footprints=True, color="red")
    m.enableArrowKey(a)

    #creates a separate thread to manage the timer
    timer_thread = threading.Thread(target=start_timer, args=(60,), daemon=True)
    timer_thread.start()

    #checking if the user has finished the maze before 60 seconds
    while (a.x, a.y) != (1, 1):
        if time_up:
            print("\nTIME'S UP!")
            break 
        
        try:
            m._win.update()
        except:
           
            break
    
    m._win.destroy()
    return not time_up 

#Explaining the game to the user, first thing the user will see
print("")
print("You have made it to Granny's house!")
time.sleep(2)
print("However in order to enter you must navigate her front yard by competing a maze")
time.sleep(2)
print("You have 3 chances to complete the maze in 60 seconds, the screen will reload each time")
time.sleep(2.5)
print("Use your arrow keys to move!")
time.sleep(2)
print("Good Luck!")
time.sleep(2)

#Since this game runs 3 rounds, we need a counter to keep track
rounds = 0

#Checking if the user has won or not
won = False

#Runs the 3 rounds
while rounds < 3:

    #Updating the rounds after one chance
    rounds += 1

    #calling the maze function so the user can play
    success = makemaze()

    #checking if the user has finished and victory message then breaking the loop
    if success:
        time.sleep(3)
        print("Victory! You made it through!")
        won = True
        break

    #telling the user how many more rounds are left
    else:
        if rounds == 1:
            print("You have 2 more chances!")
        elif rounds == 2:
            print("Oh no! Last chance!")

#what will be displayed if the user has NOT completed the maze within the 3 chances
if not won:
    print("Uh oh, you ran out of chances...")
    time.sleep(2)
    print("Wait! You found a secret path! You made it to Granny's anyway!")

