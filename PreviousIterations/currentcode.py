   # ------------------------------------------------------
#    Team Name: Smordle 
# Team Members: Kira Seshaiah and Katelyn Diaz
#        Peers: 
#   References: 
# ------------------------------------------------------
import distributor
import random

def yeetus1(inputWord: str):
  """ as it cycles through, creates a new string where if the letter is incorrect, it will put a question mark in its place, and if it is correct, it will put a dollar sign in its place
  :param inputWord: str the guess of the person playing the game
  
  """
  wordList = random.choice(list(distributor.items()))
  if checkLength(inputWord) == True: 
    replacedWord = []
    for letter in range(len(inputWord)):
      wordleWord = wordList[0]
      if wordleWord[letter] == inputWord[letter]:
        character = wordleWord[letter]
        correct = wordleWord[letter].replace(character,"$")
        replacedWord.append(correct)
      else:
        character = wordleWord[letter]
        incorrect = wordleWord[letter].replace(character,"?")
        replacedWord.append(incorrect)
    return replacedWord
  else:
    return False

def yeetus(inputWord: str):
  """ as it cycles through, creates a new string where if the letter is incorrect, it will put a question mark in its place, and if it is correct, it will put a dollar sign in its place
  :param inputWord: str the guess of the person playing the game
  
  """

wordList = ["sophia"]
  if checkLength(inputWord) == True: 
    replacedWord = []
    for letter in range(len(inputWord)):
      wordleWord = wordList[0]
      if wordleWord[letter] == inputWord[letter]:
        character = wordleWord[letter]
        correct = wordleWord[letter].replace(character,"$")
        replacedWord.append(correct)
      else:
        character = wordleWord[letter]
        incorrect = wordleWord[letter].replace(character,"?")
        replacedWord.append(incorrect)
    return replacedWord
  else:
    return False

def checkLength(inputWord: str):
  """ checks to make sure that the input word is 6 characters
  
  :param inputWord: str the input word
  :return bool: true if word is length 6 and false if it is not

  
  
  """
  if len(inputWord) == 6:
    return True
  else:
    return False

def deletus(inputWord: str): 
  """want to cycle through replacedWord to see if all characters is "$", and if so then print "congrats you got the word" and if not, then input function to input another word 
  
  :param inputWord: str the word that people input that is their guess on the Smith Wordle
  :return: bool returns that the word is true if there are no $ signs in the new word, and false if there are, or if the input word didn't fall within the necessary characteristics required 
  
  """
  x = yeetus(inputWord)
  i = 0
  if checkLength(inputWord) == True:
    for symbol in range(0,6):
      if x[symbol] == "$":
        i = i+1
    if i == 6:
      return True
    else:
      return False
  else:
    return False



def main():
  inputWord = input("What is your guess?: ")

  while deletus(inputWord) == False:
    if checkLength(inputWord) == True:
        print(list(inputWord))
        print(yeetus(inputWord))
        inputWord = input("What is your guess?: ")
    else: 
        print("Error: Word isn't six characters")
        inputWord = input("What is your guess?: ")

  if deletus(inputWord) == True:
    print(list(inputWord))
    print(yeetus(inputWord))
    print("congrats")


 # print("Program Starts")
  #print(myTestedFunction(True))

if __name__ == "__main__":  
    main()





# sources: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

# from graphics import *
# from box import *

# width = 600
# height = 400
# win = GraphWin("Smordle", width, height)
# win.setBackground("gray")

# #all things text


# inputStr = "      "

# # word lists
# wordList = inputStr
# checkList = "sophia"

# #anchor list
# a1 = Point(75,70)
# a2 = Point(165,70)
# a3 = Point(255,70)
# a4 = Point(345,70)
# a5 = Point(435,70)
# a6 = Point(525,70)

# #rectangle grid

# rectangle1 = Box(win, a1)
# rectangle2 = Box2(win, a2)
# rectangle3 = Box3(win, a3)
# rectangle4 = Box4(win, a4)
# rectangle5 = Box5(win, a5)
# rectangle6 = Box6(win, a6)

# rectangle1.draw(win)
# rectangle2.draw(win)
# rectangle3.draw(win)
# rectangle4.draw(win)
# rectangle5.draw(win)
# rectangle6.draw(win)

# win.getMouse()
# inputBox = Entry(Point(200,300), 5)
# inputBox.setSize(36)
# inputBox.draw(win)


# #letters in each box
# chrlist = list(str(wordList))
# keyPressed = win.getKey()

# while rectangle1.color(win) == False or rectangle2.color(win) == False or rectangle3.color(win) == False or rectangle4.color(win) == False or rectangle5.color(win) == False or rectangle6.color(win) == False:

  
#   #box 
#   rectangle1.color(win)
#   rectangle2.color(win)
#   rectangle3.color(win)
#   rectangle4.color(win)
#   rectangle5.color(win)
#   rectangle6.color(win)
    
#   #letters in each box
#   letter1 = Text(a1, chrlist[0])
#   letter2 = Text(a2, chrlist[1])
#   letter3 = Text(a3, chrlist[2])
#   letter4 = Text(a4, chrlist[3])
#   letter5 = Text(a5, chrlist[4])
#   letter6 = Text(a6, chrlist[5])
  
#   letter1.draw(win)
#   letter2.draw(win)
#   letter3.draw(win)
#   letter4.draw(win)
#   letter5.draw(win)
#   letter6.draw(win)

#   inputBox = Entry(Point(200,300), 5)
#   inputBox.setSize(36)
#   inputBox.draw(win)
  
# while (win.checkMouse() == None):
#   inputStr = inputBox.getText()

