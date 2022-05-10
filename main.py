# ------------------------------------------------------
#    Team Name: Will Code for Lamont Popsicles
# Team Members: Kira Seshaiah and Katelyn Diaz
#        Peers: N/A
#   References: 
#https://stackoverflow.com/questions/34602494/getting-text-from-a-entry-window-in-python-graphics
#https://www.youtube.com/watch?v=gszWqF4PKjs
#https://www.usabledatabases.com/database/books-isbn-covers/sample/#table_book
#https://www.adamsmith.haus/python/answers/how-to-get-a-random-entry-from-a-dictionary-in-python
#https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary

# ------------------------------------------------------
from graphics import *
import distributor
import random

width = 600
height = 430

def startScreen(): #opening window
  win2 = GraphWin("Smordle", width, height)
  
  introImage = Image(Point(300,215), "Images/smordle intro screen.gif")
  introImage.draw(win2)
  
  win2.getMouse() #click to close the screen
  introImage.undraw()
  win2.close()


def gameScreen(): #game window
  win = GraphWin("Smordle", width, height)
  win.setBackground("gray")
  
  #text entry box
  textEntry = Entry(Point(300,200),50)
  textEntry.draw(win)
  
  #background images for the boses
  boxImage = Image(Point(75,70), "Images/smordle box one.gif")
  box2Image = Image(Point(165,70), "Images/smordle box two.gif")
  box3Image = Image(Point(255,70), "Images/smordle box three.gif")
  box4Image = Image(Point(345,70), "Images/smordle box four.gif")
  box5Image = Image(Point(435,70), "Images/smordle box five.gif")
  box6Image = Image(Point(525,70), "Images/smordle box six.gif")
  
  boxImage.draw(win)
  box2Image.draw(win)
  box3Image.draw(win)
  box4Image.draw(win)
  box5Image.draw(win)
  box6Image.draw(win)
  
  #box outlines
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

  #error sign
  errorRectangle = Rectangle(Point(50, 130), Point(550, 170))
  errorMessage = Text(Point(300,150), "Error: word isn't 6 characters. Try again")

  
  #the word for smordle
  word = distributor.getRandomWord() #getting the word and the fact
  factWord = word[0]
  checkStr = list(factWord) #converting the word into a string
  # print(checkStr) #can uncomment to see what the smordle word is

  #starting values for printed words after entering
  i = 0 #counter for number of letters correct
  numTry = 0 #number of tries the user has done up to this point
  xcoord = 100
  ycoord = 250
  newYCoord = 0
  
  while i !=6: #need loop for the text box to work
    win.getMouse() 
    errorMessage.undraw()
    errorRectangle.undraw()
    boxImage.undraw()
    box2Image.undraw()
    box3Image.undraw()
    box4Image.undraw()
    box5Image.undraw()
    box6Image.undraw()
    i = 0
    
    text = textEntry.getText()
      
    inputStr = list(text)
  
    if len(text) != 6:
      errorRectangle.draw(win)
      errorRectangle.setFill(color_rgb(139,0,0))
      errorMessage.draw(win)
      errorMessage.setSize(18)
      errorMessage.setTextColor(color_rgb(192,192,192))
      boxImage.draw(win)
      box2Image.draw(win)
      box3Image.draw(win)
      box4Image.draw(win)
      box5Image.draw(win)
      box6Image.draw(win)
          
    else:
      #letters in each box
      letter1 = Text(Point(75,70), inputStr[0])
      letter2 = Text(Point(165,70), inputStr[1])
      letter3 = Text(Point(255,70), inputStr[2])
      letter4 = Text(Point(345,70), inputStr[3])
      letter5 = Text(Point(435,70), inputStr[4])
      letter6 = Text(Point(525,70), inputStr[5])
    
      letter1.draw(win)
      letter2.draw(win)
      letter3.draw(win)
      letter4.draw(win)
      letter5.draw(win)
      letter6.draw(win)
    
    #coloring the boxes
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
  
    #adding checks to the word
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
    
    #spacing out word
      emptyText =[]
      splitText = list(text)
      for a in range (0,6):
        spacedWord = splitText[a]
        emptyText.append(spacedWord)
      " ".join(emptyText)
      
    #printing text
      testText = Text(Point(xcoord,ycoord+numTry*40), emptyText)
      checkText = Text(Point(xcoord,ycoord+20+numTry*40), replacedWord)
      newYCoord = ycoord+numTry*40
      testText.draw(win)
      testText.setTextColor("pink")
      checkText.draw(win)
    
    #making differnt columns
      if numTry == 3 or numTry==7 or numTry==11 or numTry==15 or numTry==19:
        newColumn = (numTry+1)/4
        xcoord = xcoord +newColumn*100
        numTry = -1
  
      if xcoord >501:
        i = 6
      
      win.getMouse()
      letter1.undraw()
      letter2.undraw()
      letter3.undraw()
      letter4.undraw()
      letter5.undraw()
      letter6.undraw()
      boxImage.draw(win)
      box2Image.draw(win)
      box3Image.draw(win)
      box4Image.draw(win)
      box5Image.draw(win)
      box6Image.draw(win)
      numTry = numTry+1
  

  #end screen
  win3 = GraphWin("Smordle", width, height)
  
  if xcoord >501: #if get the word incorrect
    endImage2 = Image(Point(300,215), "Images/smordle end screen3.gif")
    endImage2.draw(win3)
 
  else: #if get the word correct
    endImage = Image(Point(300,215), "Images/smordle end screen2.gif")
    endImage.draw(win3)

    #formatting and showing the fact text
    guessedWord = Text(Point(247,155), checkStr)
    guessedWord.draw(win3)
    formatFact = word[1].replace("|", "\n")
    facts = Text(Point(195,315), formatFact)
    facts.draw(win3)


def checkLengths(inputWord: str):
  """ checks to make sure that the input word is 6 characters
  :param inputWord: str the input word
  :return bool: true if word is length 6 and false if it is not
  >>> checkLengths("happy")
  FALSE
  >>>checkLengths("sophia")
  TRUE
  """
  if len(inputWord) == 6:
    return True
  else:
    return False
  
def main():
  """ contains all of the code to play the game
  :return graphics: the game starts and then playing
  
  """
  #intro window
  startScreen()

  #game window 
  gameScreen()


if __name__ == "__main__":  
  main()

