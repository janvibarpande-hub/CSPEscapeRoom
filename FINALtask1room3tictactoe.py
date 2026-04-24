
#Used to create the wolf's (computer's) position
import random

#For pauses inbetween printing print statements
import time

#creating the spots for each coordinate in a list
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

#function for creating the board
def draw_board():
    #giving the user the letters and numbers so they know which coordiante is where
    print("   1     2    3  ")
    print("A     ║    ║     ")
    print(f"   {board[0]}  ║ {board[1]}  ║  {board[2]}  ")
    #filling in the list positions in the board spaces so an X or O can be places
    print("  ════╬════╬════ ")
    print("B     ║    ║     ")
    
    print(f"   {board[3]}  ║ {board[4]}  ║  {board[5]}  ")
    print("  ════╬════╬════ ")
   
    print(f"C  {board[6]}  ║ {board[7]}  ║  {board[8]}  ")
    print("      ║    ║     ")
    print("")

#counter to keep track of user and wolf moves combined
turns = 0

#Welcome message and instructions
print("Congratulations for making it this far into the escape room!")
print("You are now at Granny's house and the wolf has proposed a challenge to you...")
time.sleep(2)
message = "A game of TIC TAC TOE!!!"

#to create a typing effect when revealing the game
for letter in message:
    print(letter, end="", flush=True)
    time.sleep(0.1)
time.sleep(2)
print("")
print("If the wolf beats you then you will get eaten!")
print("But if you beat the wolf than he will leave you alone forever")
time.sleep(2.5)
print(" ")
print("Here is the board:")
draw_board()
time.sleep(2.5)
print(" ")
print("You are X and he is O")
print("Good luck!....Or else")
time.sleep(3)


    
#prints appropriate message for whether it is the first turn of the game or not
while turns < 9:
    if turns == 0:
        print(" ")
        print("You start!")
    elif turns!=0:
        print(" ")
        print("Your turn!")

    #getting row letter
    row = input("Enter row (A,B,C): ").upper()
    
    taking_input = True
    while taking_input:
        try:
            #getting column number and checking for correct value
            col = int(input("Enter column (1,2,3): "))
            taking_input = False
        except ValueError:
            print("Please enter the column number as 1,2 or 3")

    #every 'a' position is in the first 3 indexes
    #by taking the column number i can determine which exact index in the list is correct
    #but first 1 must be subtracted because python indexes start from 0
    if row == "A":
        index = col - 1
    elif row == "B":
        index = (col - 1) + 3  
    elif row == "C":
        index = (col - 1) + 6
    else:
        #further checking if the user has entered a invalid number/letter
        print("You did not enter a valid input")
        continue

    #checking if the position has been picked or not
    if board[index] != " ":
        print("Sorry that spot is taken")
        continue
    else:
        board[index] = "X"
        #prints updated board with marked position
        draw_board()
        #updating turns counter
        turns+= 1

    #checking every winning combination to see if the player or wolf has 3 in a line
    def check_win():
        if board[0] == board[1] == board[2] and board[0] != " ":
            return board[0] 
        elif board[3] == board[4] == board[5] and board[3] != " ":
            return board[3]
        elif board[6] == board[7] == board[8] and board[6] != " ":
            return board[6] 
        elif board[0] == board[3] == board[6] and board[0] != " ":
            return board[0]
        elif board[1] == board[4] == board[7] and board[1] != " ":
            return board[1] 
        elif board[2] == board[5] == board[8] and board[2] != " ":
            return board[2]
        elif board[0] == board[4] == board[8] and board[0] != " ":
            return board[0]
        elif board[2] == board[4] == board[6] and board[2] != " ":
            return board[2]
        elif " " not in board:
            print("It's a draw!")
        return None
    
    #placing the return value in a variable
    winner = check_win()

    #the winning combination may be occupied with marks however it has to be checked whether all 3 marks are by the same player
    if winner == "X":
        print("Congratulations you won!!")
        break
    elif winner == "O":
        print("Oh no! Wolf outsmarted you!")
        break
    
    #creating computer 'wolf' player
    print("Wolf is thinking...")
    time.sleep(3)

    comp_choice = random.randint(0, 8) 
    while board[comp_choice] != " ":
        comp_choice = random.randint(0, 8) 
    board[comp_choice] = "O"
    #printing the updated board with the wolf's 'O'
    draw_board()
    turns += 1
    check_win()
    print("Wolf played an O")
    print("")
    




    
        

    

        
