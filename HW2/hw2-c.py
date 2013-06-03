#!/usr/bin/python
import string
import sys

# load string
f = open("ciphertext.txt","r")
ciphertext = f.read()
ciphertext = ciphertext.rstrip('\n')
ciphertext = ciphertext.rstrip('\r')
f.close()

possM = range(3,6)
for m in possM:  #check each possible m, defined in possM
    rows = list() #initialize rows as a list
    
    print("m: " + str(m)) #print m heading
    for i in range(m):  #iterates from 0 to m
        row = []        #intialize list of letters (each row)
        for index in range(i,len(ciphertext),m):  #add every mth letter
                                                  #with offset i to row
            row.append(ciphertext[index])
        rows.append(row) #add row to rows list
        sys.stdout.write('>')
        for l in row:
            sys.stdout.write(l)
        sys.stdout.write('\n')
        
  
        #calculate index of coincidence for each row in rows and print it
        coincidence = float("0")
        for letter in string.lowercase:
            coincidence += float(row.count(letter) * (row.count(letter)-1))
        coincidence /= float(len(row)*(len(row)-1))
        print("I_c" + str(i+1) + ": " + str(coincidence))
    print("-----------")
