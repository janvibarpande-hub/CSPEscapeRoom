import random
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def draw_board():
    print("   1     2    3  ")
    print("A     ║    ║     ")
    print(f"   {board[0]}  ║ {board[1]}  ║  {board[2]}  ")
    
    print("  ════╬════╬════ ")
    print("B     ║    ║     ")
    
    print(f"   {board[3]}  ║ {board[4]}  ║  {board[5]}  ")
    print("  ════╬════╬════ ")
   
    print(f"C  {board[6]}  ║ {board[7]}  ║  {board[8]}  ")
    print("      ║    ║     ")
    print("")


turns = 0

print("Congratulations for making it this far into the escape room!")
print("You are now at Granny's house and the wolf has proposed a challenge to you...")
time.sleep(2)
message = "A game of TIC TAC TOE!!!" # 📦 The text we want to print

for letter in message:
    print(letter, end="", flush=True)
    time.sleep(0.3)
print("")
print("If the wolf beats you then you will get eaten!")
print("But if you beat the wolf than he will leave you alone forever")
time.sleep(2)
print("You are X and he is O")
print("Good luck!....Or else")
time.sleep(3)
    


while turns < 9:
    if turns == 0:
        print("You start!")
    elif turns!=0:
        print("Your turn!")
    row = input("Enter row (A,B,C): ").upper()
    col = int(input("Enter column (1,2,3): "))
    
    if row == "A":
        index = col - 1
    elif row == "B":
        index = (col - 1) + 3  # What number moves us to the second row?
    elif row == "C":
        index = (col - 1) + 6
    else:
        print("You did not enter a valid input")
        continue
    
    if board[index] != " ":
        print("Sorry that spot is taken")
        continue
    else:
        board[index] = "X"
        draw_board()
        turns+= 1
        
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
    winner = check_win()
    if winner == "X":
        print("Congratulations you won!!")
        break
    elif winner == "O":
        print("Oh no! Wolf outsmarted you!")
        break
    

    print("Wolf is thinking...")
    time.sleep(3)

    comp_choice = random.randint(0, 8) 
    while board[comp_choice] != " ":
        comp_choice = random.randint(0, 8) 
    board[comp_choice] = "O"
    draw_board()
    turns += 1
    check_win()
    print("Wolf played an O")
    print("")
    




    
        

    

        
