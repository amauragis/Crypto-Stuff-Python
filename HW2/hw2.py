#!/usr/bin/python
import os, re
from os.path import join, abspath, isfile, isdir, exists, basename
from shutil import copyfile, copytree, rmtree
from time import strftime, strptime, localtime
import operator
import string
from operator import itemgetter

class Freq:
    def __init__(self, txt):
        self.count = self.doCount(txt)
    
    def doCount(self, txt):
        dict = {}
        for c in txt:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        return dict

    def get(self):
        return self.count

    def __str__(self):
        items = self.count.items()
        items.sort(key=itemgetter(1), reverse=True)
        rval = []
        for i in items:
            rval.append(i.__str__())
         
        return "\n".join(rval)
        
    def __getitem__(self, i):
        try:
            return self.count[i]
        except KeyError:
            return 0

# load string
f = open("ciphertextTEST.txt","r")
ciphertext = f.read()
ciphertext = ciphertext.rstrip('\n')
ciphertext = ciphertext.rstrip('\r')
f.close()

#init string index and storage map
strInd = 0
trigrams = dict()
letterProbability = dict({'A':.082, 'B':.015, 'C':.028, 'D':.043, 'E':.127, 'F':.022, 'G':.020, 'H':.061,
                          'I':.070, 'J':.002, 'K':.008, 'L':.040, 'M':.024, 'N':.067, 'O':.075, 'P':.019,
                          'Q':.001, 'R':.060, 'S':.063, 'T':.091, 'U':.028, 'V':.010, 'W':.023, 'X':.001,
                          'Y':.020, 'Z':.001})

#search text for trigrams, storing each trigram as a key, and a list of 1st char positions as a value
for strInd in range(len(ciphertext)-2):
    key = ciphertext[strInd:strInd+3]
    if key in trigrams:                     #this is 2nd or greater occurence of trigram
        trigrams[key].append(strInd+1)      #1 must be added to the index because 0 indexing makes the math harder
    else:                                   #first occurence of trigram
        trigrams[key] = list([strInd+1])    #1 must be added to the index because 0 indexing makes the math harder

#remove trigrams that only occur once
for key in trigrams.copy():
    if len(trigrams[key]) <= 1:
        trigrams.pop(key)

#sort trigrams for printing
sortedTrigrams = sorted(trigrams.iteritems(), key=operator.itemgetter(1))
print("""
(a) Trigrams that occur more than once, sorted by initial start position.
--------------------------------------------------------------------------""")
for entry in sortedTrigrams:
    print(str(entry))

print("""
--------------------------------------------------------------------------
""")
possM = [1, 2, 3, 4, 5, 6]
for m in possM:
    rows = list()
    rowLen = len(ciphertext) // m
    rowPos1 = 0
    rowPos2 = rowLen
    print(m)
    for row in range(m):
        row = ciphertext[rowPos1:rowPos2]
        rows.append(row)
        rowPos1 = rowPos2
        rowPos2 = rowPos2+rowLen
        coincidence = float("0")
        for letter in string.lowercase:
            #print(str(letter)+": " + str(Freq(row)[letter]))
            #print((float(Freq(row)[letter] * (Freq(row)[letter]-1))) / float(len(row)*(len(row)-1)))
            coincidence += float(row.count(letter) * (row.count(letter)-1))
            #print(coincidence)
        coincidence /= float(len(row)*(len(row)-1))
        #print(row)
        print(str(coincidence))
    
    
