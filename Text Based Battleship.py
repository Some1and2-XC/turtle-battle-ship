import random

#Largest Boat Possible
ammountOfBoats = 6

#Smallest Boat Possible
minimumBoat = 1

#Board length, should be 10 or less
bLen = 10

#This is for seeing if you won yet
noOfBoatParts = 0

acceptedNo = []
def drawB(gb):
 global bLen
 drawL(bLen * 2)
 print()
 print("     ", end="")
 for i in range(0, bLen):
     print(str(i) + "  ", end="")
 print()
 print()

 for i in range(0, bLen):
     print(i, " ", end="")
     for j in range(0, bLen):
          if gb[i][j] == "-" or gb[i][j] == "'":
              print(" ", gb[i][j], end="")

          else:
              if gb[i][j] <= ammountOfBoats:
                  print("  -", end="")
              else:
                  isIn = False
                  for k in range(0, bLen):
                      if int(gb[i][j]) - ammountOfBoats in gb[k]:
                          isIn = True
                  if isIn is False:
                      print(" ", gb[i][j] - ammountOfBoats, end="")
                  else:
                      print("  x", end="")
     print()
 print()
 drawL(bLen * 2)

def drawL(length):
 for i in range(0, length):
     print("+=", end="")
 print()

def randLabel(boatLen):
 global bLen, board, noOfBoatParts
 isVert = random.randint(0, 1)
 it = 1000
 isFound = False
 while isFound is False and it:
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
     it += 1

 for i in range(0, boatLen):
     if isVert == 1:
         board[y + i][x] = boatLen
     else:
         board[y][x + i] = boatLen
     noOfBoatParts += 1



board = []

# y Dir
for i in range(0, bLen * 2 + 1):
  acceptedNo.append(str(i))
for i in range(0, bLen):
 board.append([])
 # x Dir
 for j in range(0, bLen):
     board[i].append("-")
for i in range(ammountOfBoats, minimumBoat - 1, -1):
 randLabel(i)
drawB(board)
win = False
noOfGuesses = 0
while win is False:
  guessConfirmed = False
  while guessConfirmed is False:
      guessI = input("Which Row?")
      guessJ = input("Which Collum")
      if guessI in acceptedNo and guessJ in acceptedNo:
          guessI = int(guessI)
          guessJ = int(guessJ)
          guessConfirmed = True
      else:
          print("Out of Range")
          print(guessI)
          print(guessJ)
  else:
      noOfGuesses += 1

      if str(board[guessI][guessJ]) in acceptedNo:
          if board[guessI][guessJ] <= ammountOfBoats:
              board[guessI][guessJ] = board[guessI][guessJ] + ammountOfBoats
              noOfBoatParts -= 1
      else:
          board[guessI][guessJ] = "'"
  if noOfBoatParts == 0:
      win = True
  drawB(board)
print("You WIN!", "in", noOfGuesses, "guesses")


