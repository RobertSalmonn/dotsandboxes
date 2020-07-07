import turtle

wn=turtle.Screen()
wn.setup(width=700, height=700)
wn.tracer(0)

turn=1
counter=0

class Pen (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.shape("circle")
        self.color("black")
        self.speed(0)

lines=[]

class H (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shapesize(stretch_wid=0.1, stretch_len=5)
        self.shape("square")
        self.color("grey")
        self.speed(0)

class V (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=0.1)
        self.shape("square")
        self.color("grey")
        self.speed(0)

r=0
b=0

class Square (turtle.Turtle):
    def __init__(self):
        global r
        global b
        turtle.Turtle.__init__(self)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=5)
        self.shape("square")
        if turn==1:
            self.color("red")
            r+=1
        else:
            self.color("blue")
            b+=1
            
        self.speed(0)



dot=Pen()

arr=[[9,0,9,0,9,0,9,0,9,0,9,0,9],
     [0,8,0,8,0,8,0,8,0,8,0,8,0],
     [9,0,9,0,9,0,9,0,9,0,9,0,9],
     [0,8,0,8,0,8,0,8,0,8,0,8,0],
     [9,0,9,0,9,0,9,0,9,0,9,0,9],
     [0,8,0,8,0,8,0,8,0,8,0,8,0],
     [9,0,9,0,9,0,9,0,9,0,9,0,9],
     [0,8,0,8,0,8,0,8,0,8,0,8,0],
     [9,0,9,0,9,0,9,0,9,0,9,0,9],
     [0,8,0,8,0,8,0,8,0,8,0,8,0],
     [9,0,9,0,9,0,9,0,9,0,9,0,9],
     [0,8,0,8,0,8,0,8,0,8,0,8,0],
     [9,0,9,0,9,0,9,0,9,0,9,0,9]]

for i in range (13):
    for j in range (13):
        if arr[i][j]==9:
            
            dot.goto((j-6)*50,((i*-1)+6)*50) 

            dot.stamp()


def calc(x, y):

    row=round((x/50)+6)
    col=round(((y*-1)/50)+6)
    
    check(col, row)

def check(c, r):
    if arr[c][r]==0:
        check_row(c, r)
    else:
        pass

def check_row(c, r):
    global turn
    global counter
    orientation=""
##    print (c, r)
    if (r+2)%2==0:
##        print ("vertical")
        line=V()
        orientation="v"
 
    else:
##        print ("horizontal")
        line=H()
        orientation="h"

    if turn==1:
        line.color("red")

    else:
        line.color("blue")

    counter+=1
##    print (counter)
    line.goto((r-6)*50,((c*-1)+6)*50)
    lines.append(line)
    arr[c][r]=1
    

    box(c, r, orientation)

def box(c, r, o):

    global counter
    point=False
    if o=="v":
        if r+2<13 and c-1>-1 and c+1<13:
            if arr[c+1][r+1]==1 and arr[c][r+2]==1 and arr[c-1][r+1]==1:
##                print ("right")
                s=Square()
                s.goto(((r-6)*50+50),((c*-1)+6)*50)
                lines.append(s)
                point=True
                
        if r-2>-1 and c+1<13 and c-1>-1:
            if arr[c+1][r-1]==1 and arr[c][r-2]==1 and arr[c-1][r-1]==1:
##                print ("left")
                s=Square()
                s.goto(((r-6)*50-50),((c*-1)+6)*50)
                lines.append(s)
                point=True


    else:
        if c-2>-1 and r+1<13 and r-1>-1:
            if arr[c-1][r+1]==1 and arr[c-1][r-1]==1 and arr[c-2][r]==1:
##                print("up")
                s=Square()
                s.goto(((r-6)*50),(((c*-1)+6)*50)+50)
                lines.append(s)
                point=True

                
        if c+2<13 and r+1<13 and r-1>-1:
            if arr[c+1][r+1]==1 and arr[c+1][r-1]==1 and arr[c+2][r]==1:
##                print("down")
                s=Square()
                s.goto(((r-6)*50),(((c*-1)+6)*50)-50)
                lines.append(s)
                point=True
    if counter==84:
        winner()
    else:        
        next_turn(point)


def next_turn(p):
    global turn
    if p==True:
        pass
    else:
        if turn==1:
            turn=2
        else:
            turn=1


def winner():
    global r
    global b
    l=Pen()
    l.goto(0,300)
    if r>b:
        
        l.write("Red wins!", align="center", font=("Calibri", 30))
    elif b>r:
        l.write("Blue wins!", align="center", font=("Calibri", 30))
    else:
        l.write("Draw!", align="center", font=("Calibri", 30))    












wn.listen()
wn.onscreenclick(calc)


while True:
    wn.update()
