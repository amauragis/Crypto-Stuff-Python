#!/usr/bin/python

################################################################################
# hmwk2_partB.py
# Branden Ghena
#
# A python program for Cryptography Hmwk 2 Part B
#   Takes a list of ciphertext and rewrites it into m columns where m is the
#   guess for the size of the key. Then finds the index of coincidence for the
#   row
# 
################################################################################

# Import the string library
import string

testing = True

# Ciphertext from Hmwk 2
ciphertext = 'vhtuqduovhtfkspqtibspoksnwgwvttbdyxhclxopabstiropajhjogacrxcruocqrxuknpznyeidlxgjeswpiirgtpwnsivgsictydtcfxqviiwquhgkcxzkacaciptcmxzabpggdxbpelmqrzqktnopdacpgtoehpbfhtofespaddbxiiceogzgocsyhdpgcpagsnbqnnaquhkktwhjexhclxopmptkaivgndjglrcxepo'

# Create the empty lists
list3 = [[], [], []]
list4 = [[], [], [], []]
list5 = [[], [], [], [], []]
list8 = [[], [], [], [], [], [], [], []]

# Create the new matrices
for index in range(len(ciphertext)):
    letter = ciphertext[index]
    list3[index % 3].append(letter)
    list4[index % 4].append(letter)
    list5[index % 5].append(letter)
    list8[index % 8].append(letter)

# Print the lists
#if testing:
#    print list3
#    print list4
#    print list5
#    print list8

# Create index of coincidence lists
i_c3 = [0., 0., 0.]
i_c4 = [0., 0., 0., 0.]
i_c5 = [0., 0., 0., 0., 0.]
i_c8 = [0., 0., 0., 0., 0., 0., 0., 0.,]

# Find the index of coincidence for m=3
for index in range(len(list3)):
    for letter in string.lowercase:
        freq = list3[index].count(letter)
        i_c3[index] += freq*(freq-1)
    n = len(list3[index])
    i_c3[index] = (i_c3[index]/(n*(n-1)))

# Find the index of coincidence for m=4
for index in range(len(list4)):
    for letter in string.lowercase:
        freq = list4[index].count(letter)
        i_c4[index] += freq*(freq-1)
    n = len(list4[index])
    i_c4[index] = (i_c4[index]/(n*(n-1)))

# Find the index of coincidence for m=5
for index in range(len(list5)):
    for letter in string.lowercase:
        freq = list5[index].count(letter)
        i_c5[index] += freq*(freq-1)
    n = len(list5[index])
    i_c5[index] = (i_c5[index]/(n*(n-1)))

if testing:
    # Find the index of coincidence for m=8
    for index in range(len(list8)):
        for letter in string.lowercase:
            freq = list8[index].count(letter)
            i_c8[index] += freq*(freq-1)
        n = len(list8[index])
        i_c8[index] = (i_c8[index]/(n*(n-1)))

# Print the results
print "m=3:", ", ".join(str(item) for item in i_c3)
print "m=4:", ", ".join(str(item) for item in i_c4)
print "m=5:", ", ".join(str(item) for item in i_c5)

if testing:
    print "m=8:", ", ".join(str(item) for item in i_c8)

