# ------------------------------------------------------
#    Team Name:  Smordle
# Team Members: Katelyn Diaz and Kira Seshaiah
#        Peers: N/A
#   References: N/A
# ------------------------------------------------------
""" This Python script is for you to test your code before submitting it. 

Usage: click "Shell" next to "Console", then type "python3 tests.py" as shown below:
~/Final-Project$ python3 testsuite.py
"""
import unittest
from main import *
from distributor import *
import random



class SimpleTest(unittest.TestCase):
  def test_getHeader(self):
  #   header = []
  #   # self.assertEqual(getHeader(), ['word', ' fact'])
  #   self.assertEqual(getHeader(), [])
    self.assertIsInstance(getHeader(), list)

  def test_checkLength(self): #  Checks checkLength *WORKS*
    self.assertEqual(checkLengths("sophia"), True)
    self.assertEqual(checkLengths("happy"), False)

  # def test_getRandomWordList(self):
  #   self.assertIsInstance(type(getRandomWordList("sophia")), list)

  # def test_readDatabase(self):
  #   self.assertIsInstance(type(readDatabase(), dict))


  # def test_getRandomWordList(self):
  #   random.seed(123)
  #   numWords = ["jordan"]
  #   self.assertEqual(getRandomWordList("jordan"), [j,o,r,d,a,n])
    #self.assertEqual(getRandomWordList("sophia"), [s,o,p,h,i,a])

  #     self.assertEqual(gameScreen("sophia"), "s o p h i a")
  #     # self.assertEqual(checkLength("ellie"), False)

  # def test_getRandomWord(self):
  #   self.assertEqual(distributor/getRandomWord(),[])



if __name__ == '__distributor__':
 unittest.distributor()






    



if __name__ == '__main__':  
  unittest.main()
