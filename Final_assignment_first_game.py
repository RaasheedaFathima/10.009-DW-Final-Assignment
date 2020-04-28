import turtle
import math

# 1. set up the window
wn = turtle.Screen()
wn.bgcolour("black")
wn.title("Maze Runner")
wn.setup(700,700)

class Pen(turtle,Turtle):
    def __init__(self):
        turtle.turtle.__init__(self)
        self.shape("square")
        self.colour("white")
        self.penup()
        self.speed(0) #animation speed

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.colour("red")
        self.penup()
        self.speed(0)
        self.gold = 0
        
#     direction of the player
    def move_left(self):
        move_to_x = player.xcoor() - 24
        move_to_y = player.ycoor() 
#         if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
    
    def move_right(self):
        move_to_x = player.xcoor()+ 24
        move_to_y = player.ycoor() 
#         if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    
    def move_up(self):
        move_to_x = player.xcoor()
        move_to_y = player.ycoor() +24
#         if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
        
    def move_down(self):
        move_to_x = player.xcoor()
        move_to_y = player.ycoor() - 24
#         if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
            
    def gain_gold(self,other): #to ensure that the player is touching the gold coin
        a = self.xcoor()- other.xcoor()
        b = self.ycoor() - other.ycoor()
        distance = math.sqrt( (a ** 2) + (b ** 2))
        
        if distance < 4: # there is a gold obtained
            return True
        else:
            return False
        
        
class Gold(turtle.Turtle):
    def __init__(self,x,y): #x and y coordinates is where we want our gold coin to appear
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.colour("gold")
        self.penup()
        self.speed(0)
        self.gold=100
        self.goto(x,y)
        
    def eat_up(self):
        self.goto(2000,2000)
        self.hideturtle()
        
# create a level (i will create 2 levels) 

levels = [""]

# level 1 
level_1=[
    "XXXXXXXXXXXXXXXXXXXX",
    "X PXXXXXXXXXXXXXXXXX",
    "X  XXXXXXXX  XXXXXXX",
    "X     XXXXXX  XXXXXX",
    "X       XXXX   XXXXX",
    "XXXXX   XXXXX  G XXX",
    "XXXXXX  XXXX   XXXXX",
    "XXXXXX  XXX  XXXXXXX",
    "XXXXXXX      XXXXXXX",
    "XXXXXXXX  XXXXXXXXXX",
    "XXXXXXXX     XXXXXXX",
    "XXXXXXXX     XXXXXXX",
    "XXXXXXXXXXX   XXXXXX",
    "XXXXXXXXXXX    XXXXX",
    "XXXXXXXXXXXX   GXXXX",
    "XXXXXXXXXXX    XXXXX",
    "XXXXXXXXXX   XXXXXXX",
    "XXXXXXXXXG   XXXXXXX",
    "XXXXXXXXXXX   XXXXXX",
    "XXXXXXXXXXXXXXXXXXXX",   
]


level_2=[
    "XXXXXXXXXXXXXXXXXXXX",
    "X P XXXXXXXXXXXXXXXX",
    "XX        XXXXXXXXXX",
    "XXXXXXXX      XXXXXX",
    "XXXXXXXXXXXX   XXXXX",
    "XXXXXG  XXXXX    XXX",
    "XXXXXX  XXXX   XXXXX",
    "XXXXXX  XXX  XXXXXXX",
    "XXXXXXX      XXXXXXX",
    "XXXXXXXX  XXXXXXXXXX",
    "XXXXXXXX     XXXXXXX",
    "XXG XXXX     XXXXXXX",
    "XXX  XXXXXX   XXXXXX",
    "XXX  XXXXXX    XXXXX",
    "XXX            GXXXX",
    "XXXXX  XXXXXXXXXXXXX",
    "XXXXX  XXXXXXXXXXXXX",
    "XXXXX    XXXXXXXXXXX",
    "XXXXXXX      XXXXXXX",
    "XXXXXXXXXXXXXXXXXXXX",   
]


level_3=[
    "XXXXXXXXXXXXXXXXXXXX",
    "X PXXXXXXXXXXXXXXXXX",
    "X  XXXXXXXXXXXXXXXXX",
    "X     XXXXXXXXXXXXXX",
    "X       XXXXXXXXXXXX",
    "XXXXX   XXXXXXXXXXXX",
    "XXXXXX  XXXXXXXXXXXX",
    "XXXXXX        XXXXXX",
    "XXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXXXXX   XXXX",
    "XXXXXXXXXX G  XXXXX",
    "XXXXXXX     XXXXXXXX",
    "XXXXXXXX       XXXXX",
    "XXXXX G     XXXXXXXXX",
    "XXXXXXXX      XXXXXX",
    "XXXXXX     XXXXXXXXX",
    "XXXXXXXX   XXXXXXXXX",
    "XXXXXXXXX    XXXXXXX",
    "XXXXXXXXXXX   XXXXXX",
    "XXXXXXXXXXXXXXXXXXXX",   
]

# gold list
golds = []



# add level to maze list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)

def setup_maze(level):
    for y in range (len(level)):
        pin = level [y][x]
        maze_x = -288 + (x * 24) # CALCULATE THE X AND Y COORDINATES OF THE PIN
        maze_y = 288 - (y * 24 )
        
        if pin == "X": #if Player hits the wall aka "X",
            pen.goto(maze_x,maze_y)
            pen.stamp()
            walls.append((maze_x,maze_y))
            
        if pin == "P": #P is where the player is at 
            player.goto(maze_x,maze_y)
        if pin == "G":
            gold.append(gold(maze_x,maze_y))
            
        
        
        
        
# class instance
pen = pen()
player = Player()

# coordinate list
walls = []
print (walls)

# Seting up the level
setup_maze(level[1])

# keyboard functions
turtle.listen()
turtle.onkey(player.move_left,"Left") #square will move left when the left key is clicked on the keyboard
turtle.onkey(player.move_right,"Right") #square will move right when the left key is clicked on the keyboard
turtle.onkey(player.move_up,"Up") #square will move up when the left key is clicked on the keyboard
turtle.onkey(player.move_down,"Down") #square will move down when the left key is clicked on the keyboard




wn.tracer(0)

# main game loop
while True:
    for gold in golds:
        if player.gain_gold(gold):
            player.coin += gold.coin
            print ("Player Coin: {}".format(player.coin))
            gold.destroy() #gold is destroyed once it touches the pin
            golds.remove() #remove the cold from the golds list
    wn.update()
