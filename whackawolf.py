import tkinter as tk
import random
import time


print("Whack a Wolf!")
print("Whack the wolf as many times as possible")

time.sleep(3)

def click_sound():
	root.bell()

def game_over_sound():
	root.bell()

root = tk.Tk()
root.geometry("500x500")
root.title("🐺 Whack a Wolf")
root.resizable(False,False)

score = 0
time_left = 30
game_running = False

canvas = tk.Canvas(root,width=500,height=350, bg="lightgreen")
canvas.pack()

mole = canvas.create_text(250,150,text="🐺",font=("Arial",40),state="hidden",tags="mole")

def start():
	global score, time_left, game_running
	score = 0
	time_left = 30
	game_running = True
	score_lbl.config(text="Score:0")
	timer_lbl.config(text="Time:30")
	result_lbl.config(text="")
	update_timer()
	move_mole()


def update_timer():
 	global time_left
 	if game_running:
 		if time_left>0:
 			time_left -= 1
 			timer_lbl.config(text=f"Time: {time_left}")
 			root.after(1000,update_timer)
 		else:
 			end_game()

def move_mole():
 	if game_running:
 		x = random.randint(50,450)
 		y = random.randint(50,350)
 		canvas.coords(mole,x,y)
 		canvas.itemconfigure(mole, state="normal")
 		root.after(700,move_mole)

def hit_mole(event):
 	global score
 	if game_running:
 		score += 1
 		score_lbl.config(text=f"Score:{score}")
 		click_sound()
 		canvas.itemconfigure(mole, state="hidden")


canvas.tag_bind("mole","<Button-1>",hit_mole)

def end_game():
 	global game_running
 	game_running = False
 	canvas.itemconfigure(mole, state="hidden")
 	result_lbl.config(text=f"Game Over! Final score is {score}")
 	game_over_sound()

title_lbl = tk.Label(root, text="Whack-a-Wolf", font=("Arial",18,"bold"))
title_lbl.pack()
timer_lbl = tk.Label(root,text="Time:30",font=("Arial",14))
timer_lbl.pack()
score_lbl = tk.Label(root,text="Score:0",font=("Arial",14))
score_lbl.pack()

start_btn = tk.Button(root, text="Start Game", font=("Arial",14),command=start)
start_btn.pack()

result_lbl = tk.Label(root, text="", font=("Arial",14))
result_lbl.pack()

root.mainloop()







