import turtle
wn = turtle.Screen()
wn.title("Turtle Maze Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.tracer(0)


maze = turtle.Turtle()
maze.shape("turtle")
maze.color("black")
maze.pensize(2)
maze.penup()
maze.goto(-200,200)
maze.pendown()

def draw_maze():
    #HORIZONTAL LINES
    #Row 1
    maze.forward(400)
    maze.penup()
    #Row 2
    maze.goto(-200,160)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(120)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    #Row 3
    maze.goto(-200,120)
    maze.goto(-120,120)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(120)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Row 4
    maze.goto(-160,80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(120)
    maze.penup()
    #Row 5
    maze.goto(-160,40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(120)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Row 6
    maze.goto(-120,0)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(120)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Row 7
    maze.goto(-160,-40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Row 8
    maze.goto(-200,-80)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    #Row 9
    maze.goto(-160,-120)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(240)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    #Row 10
    maze.goto(-160,-160)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Row 11
    maze.goto(-200,-200)
    maze.pendown()
    maze.forward(400)
    maze.penup()

    #VERTICAL LINES
    #Column 1
    maze.goto(-200,200)
    maze.right(90)
    maze.pendown()
    maze.forward(360)
    maze.penup()
    #Column 2
    maze.goto(-160,160)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 3
    maze.goto(-120,160)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 4
    maze.goto(-80,200)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 5
    maze.goto(-40,160)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    #Column 6
    maze.goto(0,200)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(120)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 7
    maze.goto(40,160)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 8
    maze.goto(80,200)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 9
    maze.goto(120,80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(40)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 10
    maze.goto(160,120)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(80)
    maze.penup()
    maze.forward(80)
    maze.pendown()
    maze.forward(40)
    maze.penup()
    #Column 11
    maze.goto(200,160)
    maze.pendown()
    maze.forward(360)
    maze.penup()
    maze.hideturtle()
    
    
    
    
    
    
    
    
    

            
    
    
    
    
    
    

draw_maze()




#def draw_maze()   

#setting up turtle player
player = turtle.Turtle()
player.shape("turtle")
player.color("red")
player.penup()
player.speed(0)
player.goto(-240, -180)



#moving th turtle when keys are pressed
def move_up():
    
    player.setheading(90)
    player.pendown()
    player.forward(10)
    

def move_down():
    player.setheading(270)
    player.pendown()
    player.forward(10)

def move_left():
    player.setheading(180)
    player.pendown()
    player.forward(10)




def move_right():
    player.setheading(0)
    player.pendown()
    player.forward(10)


wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

wolf = turtle.Turtle()
wolf.color("gray")
wolf.shape("turtle")
wolf.penup()
wolf.goto(-280,-180)

#while True:
    # The Follower logic:
    # It looks at the leader and moves slightly slower (e.g., speed 2)
    #wolf.setheading(wolf.towards(player))
    
    # Optional: Only move if the distance is greater than 20 
    # This prevents the follower from "jittering" when it catches up
    #if wolf.distance(player) > 20:
        #wolf.forward(2)

    #wn.update()







while True:
    wn.update()



