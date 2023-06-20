import random, turtle


#Largest Boat Possible
ammountOfBoats = 5

#Smallest Boat Possible
minimumBoat = 2

#Board length, should be 10 or less
bLen = 10

#This is for seeing if you won yet
noOfBoatParts = 0

#size of the screen
scrLen = 800

#Size ratio
sRy = 0.44
sRx = 0.4

board = []

acceptedNo = []

useFileImport = False
if useFileImport is True:

   file = open("C:\\Users\\tmk325508\\Desktop\\grid.txt", "r")
   for line in file:
       line.strip("\n")
       board.append(line)
       if line != 0:
           noOfBoatParts += 1
   file.close()


def drawB(gb):
   global bLen, guessI, guessJ, acceptedNo, noOfBoatParts, noOfGuesses
   i = guessI
   j = guessJ

   if gb[i][j] == "-":
      pen.color("black")
      pen.pencolor("white")
      squareDraw(guessJ, guessI)
      gb[i][j] = "'"
      noOfGuesses += 1


   elif gb[i][j] != "'":
      isIn = True
      if 0 < gb[i][j] <= ammountOfBoats:
          pen.color("red")
          pen.pencolor("white")
          gb[i][j] += ammountOfBoats
          squareDraw(guessJ, guessI)
          isIn = False
          noOfGuesses += 1
          for k in range(0, bLen):
              if gb[i][j] - ammountOfBoats in gb[k]:
                  isIn = True

      toFind = gb[i][j]

      if isIn is False:
          for m in range(0, bLen):
              for l in range(0, bLen):
                  if str(gb[m][l]) in acceptedNo:
                      if gb[m][l] == toFind:
                          pen.color("cyan")
                          pen.pencolor("white")
                          gb[m][l] += ammountOfBoats
                          squareDraw(l, m)
                          noOfBoatParts -= 1


   return


def randLabel(boatLen):
 global bLen, board, noOfBoatParts
 isVert = random.randint(0, 1)
 isFound = False
 while isFound is False:
     isVert = random.randint(0, 1)

     x = random.randint(0, bLen - 1)
     y = random.randint(0, bLen - 1)
     isFound = True
     for i in range(0, boatLen):
         if isVert == 1:
             if y + i >= bLen:
                 isFound = False
             elif board[y + i][x] != "-":
                 isFound = False
         else:
             if x + i >= bLen:
                 isFound = False
             elif board[y][x + i] != "-":
                 isFound = False
 boats.append([boatLen, boatLen])
 for i in range(0, boatLen):
     if isVert == 1:
         board[y + i][x] = boatLen
     else:
         board[y][x + i] = boatLen
     noOfBoatParts += 1
 return

def squareFind(a, b):
   global scrLen, zoomNo, guessI, guessJ
   y = (b + sRy * scrLen + 0.5 * zoomNo) / zoomNo
   x = (a + sRx * scrLen + 0.5 * zoomNo) / zoomNo
   if 0 <= x <= bLen:
       if 0 <= y <= bLen:
           y = int(y)
           x = int(x)
           guessJ = x
           guessI = y
           clicked = True

def squareDraw(x, y):
   global guessI, guessJ, noOfBoatParts
   if 0 <= x <= bLen:
       if 0 <= y <= bLen:
           y = int(y)
           x = int(x)
           pen.goto(x * zoomNo - sRx * scrLen, y * zoomNo - sRy * scrLen)
           pen.stamp()
           pen.goto(scrLen * 2, scrLen * 2)

def play(x, y):
    global guessI, guessJ, board, win, noOfGuesses, noOfBoatParts
    if win is False:
       squareFind(x, y)

       drawB(board)

       if noOfBoatParts <= 0:
           win = True
           pen.goto(-0.5 * scrLen + 50, 0.5 * scrLen - 85)
           t = "You WIN! in " + str(noOfGuesses) + " Guesses!"
           pen.color("black")
           pen.write(t, align="left", font=("times", 50, "normal"))
           pen.goto(scrLen * 2, scrLen * 2)
           myWindow.exitonclick()
       boatsLeft = []




boats = []

zoomNo = (scrLen - 100) / bLen
myWindow = turtle.Screen()
myWindow.title("Battleship")
turtle.setup(scrLen - 75, scrLen)
pen = turtle.Turtle()
pen.speed(0)
pen.turtlesize((zoomNo) * 0.049)
pen.penup()
pen.hideturtle()
pen.shape("square")
pen.color('white')
pen.pencolor('black')

text = turtle.Turtle()
text.hideturtle()

#initialisation
for i in range(0, bLen):
   for j in range(0, bLen):
       x = j * zoomNo - sRx * scrLen
       y = i * zoomNo - sRy * scrLen
       pen.goto(x, y)
       pen.stamp()
pen.goto(scrLen * 2, scrLen * 2)





# y Dir
for i in range(0, bLen * 2 + 1):
  acceptedNo.append(str(i))
if useFileImport is False:
   for i in range(0, bLen):
     board.append([])
     # x Dir
     for j in range(0, bLen):
         board[i].append("-")
   for i in range(ammountOfBoats, minimumBoat - 1, -1):
     randLabel(i)


win = False
noOfGuesses = 0
myWindow.onscreenclick(play)


myWindow.mainloop()

