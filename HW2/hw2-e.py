#!/usr/bin/python
import string

# load string
f = open("ciphertext.txt","r")
ciphertext = f.read()
ciphertext = ciphertext.rstrip('\n')
ciphertext = ciphertext.rstrip('\r')
f.close()

letterProbability = dict({'A':.082, 'B':.015, 'C':.028, 'D':.043,
                          'E':.127, 'F':.022, 'G':.020, 'H':.061,
                          'I':.070, 'J':.002, 'K':.008, 'L':.040,
                          'M':.024, 'N':.067, 'O':.075, 'P':.019,
                          'Q':.001, 'R':.060, 'S':.063, 'T':.091,
                          'U':.028, 'V':.010, 'W':.023, 'X':.001,
                          'Y':.020, 'Z':.001})



m = 4
rows = list()

for i in range(m):  #iterates from 0 to m
        row = []        #intialize list of letters (each row)
        #add every mth letter with offset i to row
        for index in range(i,len(ciphertext),m):  
            row.append(ciphertext[index])
        rows.append(row) #add row to rows list

for y in rows:
    print("row " + str(rows.index(y)+1))
    print("---------------------")
    for g in range(26):
        mg = float()
        for l in string.lowercase:
            mg += (float(letterProbability[l.upper()]*
                   float(y.count(chr(((ord(l)-97+g)%26)+97)))))/len(y)
        print(str(chr(g+97)) + ": " +str(mg))
    