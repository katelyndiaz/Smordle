from graphics import *
import distributor
import random

#making the window
width = 600
height = 400

win2 = GraphWin("Smordle", width, height)

introImage = Image(Point(300,215), "SmordleCover.gif")
introImage.draw(win2)

win2.getMouse()
introImage.undraw()
win2.close()


win = GraphWin("Smordle", width, height)
win.setBackground("gray")

#text box
textEntry = Entry(Point(300,200),50)
textEntry.draw(win)

#rectangles
rectangle = Rectangle(Point(35,110), Point(115, 30))
rectangle1 = Rectangle(Point(125, 110), Point(205, 30))
rectangle2 = Rectangle(Point(215,110), Point(295,30))
rectangle3 = Rectangle(Point(305,110), Point(385,30))
rectangle4 = Rectangle(Point(395,110), Point(475, 30))
rectangle5 = Rectangle(Point(485, 110), Point(565, 30))

rectangle.draw(win)
rectangle1.draw(win)
rectangle2.draw(win)
rectangle3.draw(win)
rectangle4.draw(win)
rectangle5.draw(win)

rectangle.setFill("red")
rectangle1.setFill("orange")
rectangle2.setFill("yellow")
rectangle3.setFill("light green")
rectangle4.setFill("cyan")
rectangle5.setFill("purple")

#anchor list
a1 = Point(75,70)
a2 = Point(165,70)
a3 = Point(255,70)
a4 = Point(345,70)
a5 = Point(435,70)
a6 = Point(525,70)

#dictonary
#dictValue =  

#text after the the word is inputted 
i = 0
x=0
dx = 100
dy = 250
ddy = 0
aa = 0

# def checkLength():
#   if len(text) != 6: 
#     return False
#   else:
#     return True

# def endLoop():
#   print("ur done for")
#   #go to end screen

while i !=6:
  win.getMouse()
  i = 0
  text = textEntry.getText()
  
  inputStr = list(text)
  #checkStr = list(dictValue)
  checkStr = list("sophia")

 
  #letters in each box
  letter1 = Text(a1, inputStr[0])
  letter2 = Text(a2, inputStr[1])
  letter3 = Text(a3, inputStr[2])
  letter4 = Text(a4, inputStr[3])
  letter5 = Text(a5, inputStr[4])
  letter6 = Text(a6, inputStr[5])

  letter1.draw(win)
  letter2.draw(win)
  letter3.draw(win)
  letter4.draw(win)
  letter5.draw(win)
  letter6.draw(win)


  if inputStr[0] == checkStr[0]:
    rectangle.setFill("green")
    i = i+1
  else:
    rectangle.setFill("white")
  
  if inputStr[1] == checkStr[1]:
    rectangle1.setFill("green")
    i = i+1
  else:
    rectangle1.setFill("white")

  if inputStr[2] == checkStr[2]:
    rectangle2.setFill("green")
    i = i+1
  else:
    rectangle2.setFill("white")
 
  if inputStr[3] == checkStr[3]:
    rectangle3.setFill("green")
    i = i+1
  else:
    rectangle3.setFill("white")
 
  if inputStr[4] == checkStr[4]:
    rectangle4.setFill("green")
    i = i+1
  else:
    rectangle4.setFill("white")

  if inputStr[5] == checkStr[5]:
    rectangle5.setFill("green")
    i = i+1
  else:
    rectangle5.setFill("white")
    
  replacedWord = []
  for letter in range(0,6):
    wordleWord = checkStr
    if wordleWord[letter] == inputStr[letter]:
      character = wordleWord[letter]
      correct = wordleWord[letter].replace(character,"o")
      replacedWord.append(correct)
    else:
      character = wordleWord[letter]
      incorrect = wordleWord[letter].replace(character,"x")
      replacedWord.append(incorrect)
    " ".join(replacedWord)

  emptyText =[]
  splitText = list(text)
  print(splitText)
  for n in range (0,6):
    xx = splitText[n]
    emptyText.append(xx)
  " ".join(emptyText)
  
  
  testText = Text(Point(dx,dy+x*40), emptyText)
  checText = Text(Point(dx,dy+20+x*40), replacedWord)
  ddy = dy+x*40
  testText.draw(win)
  testText.setTextColor("pink")
  checText.draw(win)
  aa = aa+1

  
  if x == 3 or x==7 or x==11 or x==15 or x==19:
    v = (x+1)/4
    dx = dx +v*100
    x = -1

  if aa == 20:
    i = 6

  
  win.getMouse()
  
  letter1.undraw()
  letter2.undraw()
  letter3.undraw()
  letter4.undraw()
  letter5.undraw()
  letter6.undraw()
  x = x+1
  print(x)
  print(i)
  print(aa)