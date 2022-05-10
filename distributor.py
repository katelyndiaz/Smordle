# ------------------------------------------------------
#    Team Name: Smordle 
# Team Members: Kira Seshaiah and Katelyn Diaz
#        Peers: CS Tutor
#   References: Library homework from class
# ------------------------------------------------------

import csv
import random

word_list = {}
header = []


def getHeader():
  """ is the header for the game
  :return str the header
  """
  return header

# def getRandomWord():
#     num = list(word_list.keys())[randint(0,len(word_list)-1)] #randint(1) was what was there before
#     return word_list[num]


def getRandomWord():
  entry_list = list(word_list.items())
  random_entry = random.choice(entry_list)
  return random_entry

def getRandomWordList(numWords): 
  """turns random word into a list
:param numWords : chr is the random word
:return new_list :list is the letters from the random word in list form
>>> getRandomWordList("jordan")
[j,o,r,d,a,n]
  """
  num = randint(0,len(word_list)-1-numWords)
  new_list = []
  for i in range(num, num+numWords):
      new_list.append(word_list[i])
  return new_list

def readDatabase():
    line_count = 0
    with open('Smordle-Dict.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if line_count == 0:
                for element in row:
                    header.append(element)
                line_count += 1
            else:
                # row.remove(row[0])
                # word_list.append(row)
                word_list[row[0]]=row[1]
                line_count += 1       
    #line_count
    return word_list

if __name__ == "__main__":
    print('Processed {0} lines.'.format(readDatabase()))
    print(f'Column names are {", ".join(header)}.')
    print(getRandomWord())
else:
    readDatabase()
    # print(word_list)
    # print(getRandomWord())