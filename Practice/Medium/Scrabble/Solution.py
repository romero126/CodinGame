import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words = []
for i in range(n):
    w = input()
    #word, match, points
    words.append([w, 0, 0])



letters = input()

#Calculate score of letters based on number of matches.
for obj in words:

    word = obj[0]
    match = obj[1]
    points = obj[2]
    #Debug("Calculate score for word",word)

    for l in range(len(word)):

        if word[l] in letters:
            #Calculate points for each letter
            #Define Points
            if word[l] in 'eaionrtlsu':
                points += 1
            elif word[l] in 'dg':
                points += 2
            elif word[l] in 'bcmp':
                points += 3
            elif word[l] in 'fhvwy':
                points += 4
            elif word[l] in 'k':
                points += 5
            elif word[l] in 'jx':
                points += 8
            elif word[l] in 'qz':
                points += 10
            if letters.count(word[l]) >= word.count(word[l]):
                match += 1

    obj[1] = match
    obj[2] = points

#Sort by Points
words = sorted(words, key=lambda x: x[2], reverse=True)
#Search match count for whole word
for i in words:
    if len(i[0]) == i[1]:
        print(i[0])
        break
