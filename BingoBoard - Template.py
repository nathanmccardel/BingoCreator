import random



tiledict = {
    1:"Insert Word 1",
    2:"Insert Word 2",
    3:"Insert Word 3",
    4:"Insert Word 4",
    5:"Insert Word 5",
    6:"Insert Word 6",
    7:"Insert Word 7",
    8:"Insert Word 8",
    9:"Insert Word 9",
    10:"Insert Word 10",
    11:"Insert Word 11",
    12:"Insert Word 12",
    13:"Insert Word 13",
    14:"Insert Word 14",
    15:"Insert Word 15",
    16:"Insert Word 16",
    17:"Insert Word 17",
    18:"Insert Word 18",
    19:"Insert Word 19",
    20:"Insert Word 20",
    21:"Insert Word 21",
    22:"Insert Word 22",
    23:"Insert Word 23",
    24:"Insert Word 24",
    25:"Insert Word 25",
    26:"Insert Word 26",
    27:"Insert Word 27",
    28:"Insert Word 28"
    
    }
#no limit to the potential length of list above

dictlength = len(tiledict)

#create tiles
#create number dictionary of integers that is length of the tile dictionary
notusedlist = list(range(1,dictlength+1))
print(dictlength)

#for each tile
#  generate a random number from 0 to tile dictionary

randomizedlist = []

for j in range(1,25):
    randomindex = random.randint(0,len(notusedlist)-1)
#    print("length of notusedlist: ", len(notusedlist))
 #   print("randomindex: ", randomindex)

    dictindex = notusedlist[randomindex]
#    print("dictionary index:", dictindex)

#    print(tiledict[dictindex])
    randomizedlist.append(tiledict[dictindex])

    del notusedlist[randomindex]
#    print()
print(randomizedlist)
iterator = 1
for item in randomizedlist:
    print(iterator)
    if iterator == 12:
        iterator = iterator + 2
    else:
        iterator = iterator + 1
    print(item)



#when button is pressed, put an X over the square
#if button has already been pressed and gets pressed again, remove the X
#dictdict = {
#    "a": tiledict,
#    
#    }
