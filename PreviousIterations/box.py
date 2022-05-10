# ------------------------------------------------------
#    Team Name: Smordle 
# Team Members: Kira Seshaiah and Katelyn Diaz
#        Peers: N/A
#   References: N/A
# ------------------------------------------------------

from graphics import *

#needs the setText for the first word, from then on out then it should be good
inputBox = Entry(Point(200,300), 5)
# inputBox.setText()


inputStr = inputBox.getText()

if len(inputStr) == 6:
  wordList = inputStr
else:
  wordList = "      "
  
checkList = "sophia"

chrlist = list(str(wordList))
print(chrlist)
chklist = list(str(checkList))

class Box:
  def __init__(self, win, position):    
    self.rectangle(position)

  def rectangle(self,position):
    p1 = Point(position.getX()+40,position.getY()+40)
    p2 = Point(position.getX()-40, position.getY()-40)
    self.body = Rectangle(p1, p2) 
    
  def draw(self,win):
    self.body.draw(win)

  def color(self,win):
    if chrlist[0] == chklist[0]:
      self.body.setFill("white")
      print("ays")
      return True
    else:
      self.body.setFill("green")
      print("nas")


class Box2(Box):
  def i__init__(self,win,position):
    super().__init__(win, position)
    self.color(win)

  def color(self,win):
    if chrlist[1] == chklist[1]:
      self.body.setFill("white")
      print("ay")
      return True
    else:
      self.body.setFill("green")
      print("na")



class Box3(Box):
  def i__init__(self,win,position):
    super().__init__(win, position)
    self.color(win)

  def color(self,win):
    if chrlist[2] == chklist[2]:
      self.body.setFill("white")
      print("ay")
      return True
    else:
      self.body.setFill("green")
      print("na")

class Box4(Box):
  def i__init__(self,win,position):
    super().__init__(win, position)
    self.color(win)

  def color(self,win):
    if chrlist[3] == chklist[3]:
      self.body.setFill("white")
      print("ay")
      return True
    else:
      self.body.setFill("green")
      print("na")

class Box5(Box):
  def i__init__(self,win,position):
    super().__init__(win, position)
    self.color(win)

  def color(self,win):
    if chrlist[4] == chklist[4]:
      self.body.setFill("white")
      print("ay")
      return True
    else:
      self.body.setFill("green")
      print("na")

class Box6(Box):
  def i__init__(self,win,position):
    super().__init__(win, position)
    self.color(win)

  def color(self,win):
    if chrlist[5] == chklist[5]:
      self.body.setFill("white")
      print("ay")
      return True
    else:
      self.body.setFill("green")
      print("na")

# class Box:
#   def __init__(self, win, position):    
#     self.rectangle(position)

#   def rectangle(self,position):
#     p1 = Point(position.getX()+40,position.getY()+40)
#     p2 = Point(position.getX()-40, position.getY()-40)
#     self.body = Rectangle(p1, p2) 
    
#   def draw(self,win):
#     self.body.draw(win)

#   def color(self,win):

#     if chrlist[0] == chklist[0]:
#       self.body.setFill("white")
#       print("ays")
#       return True
#     else:
#       self.body.setFill("green")
#       print("nas")

# class Box2(Box):
#   def i__init__(self,win,position):
#     super().__init__(win, position)
#     self.color(win)

#   def color(self,win):
#     if chrlist[1] == chklist[1]:
#       self.body.setFill("white")
#       print("ay")
#       return True
#     else:
#       self.body.setFill("green")
#       print("na")



# class Box3(Box):
#   def i__init__(self,win,position):
#     super().__init__(win, position)
#     self.color(win)

#   def color(self,win):
#     if chrlist[2] == chklist[2]:
#       self.body.setFill("white")
#       print("ay")
#       return True
#     else:
#       self.body.setFill("green")
#       print("na")

# class Box4(Box):
#   def i__init__(self,win,position):
#     super().__init__(win, position)
#     self.color(win)

#   def color(self,win):
#     if chrlist[3] == chklist[3]:
#       self.body.setFill("white")
#       print("ay")
#       return True
#     else:
#       self.body.setFill("green")
#       print("na")

# class Box5(Box):
#   def i__init__(self,win,position):
#     super().__init__(win, position)
#     self.color(win)

#   def color(self,win):
#     if chrlist[4] == chklist[4]:
#       self.body.setFill("white")
#       print("ay")
#       return True
#     else:
#       self.body.setFill("green")
#       print("na")

# class Box6(Box):
#   def i__init__(self,win,position):
#     super().__init__(win, position)
#     self.color(win)

#   def color(self,win):
#     if chrlist[5] == chklist[5]:
#       self.body.setFill("white")
#       print("ay")
#       return True
#     else:
#       self.body.setFill("green")
#       print("na")
