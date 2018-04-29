from __future__ import print_function
import sys
import os

global s1 #the first sequence being aligned
global s2 #the second sequence being aligned
global scoreTable #the dynamic programming table for finding the alignment score and path
global inputMatrix #the scoring matrix
global p #penalty of gap

#create the dynamic programming table
def create_score_table(s1len, s2len):
    global scoreTable, p, s1, s2
    scoreTable = [[0 for i in range(s2len+1)] for j in range(s1len+1)]
    for i in range(1, s2len+1):
        scoreTable[0][i] = scoreTable[0][i-1] + p
    for j in range(1, s1len+1):
        scoreTable[j][0] = scoreTable[j-1][0] + p

    for i in range(1,s1len+1):
        for j in range(1,s2len+1):
            up = scoreTable[i-1][j]+p
            left = scoreTable[i][j-1]+p
            if s1[i-1] == s2[j-1]:
                diag = scoreTable[i-1][j-1]+get_score(s1[i-1])
            else:
                diag = scoreTable[i-1][j-1]+get_score2(s1[i-1], s2[j-1])
            score = max(up, left, diag)
            scoreTable[i][j] = score
    print("Global alignment score is:" + str(scoreTable[-1][-1]))

    return

#traceback from the bottom right to the top left to find the alignmnet
def traceback():
    global s1, s2, scoreTable, p
    alignedS1 = ""
    alignedS2 = ""
    create_score_table(len(s1), len(s2))
    (row, col) = (len(s1), len(s2))

    while (row, col) != (0, 0):
        if scoreTable[row-1][col] + p == scoreTable[row][col]:
            alignedS2 = "-" + alignedS2
            alignedS1 = s1[row-1:row] + alignedS1
            (row,col) = (row-1, col)
        elif s1[row-1] == s2[col-1]:
            if scoreTable[row-1][col-1] + get_score(s1[row-1]) == scoreTable[row][col]:
                alignedS1 = s1[row-1:row] + alignedS1
                alignedS2 = s2[col-1:col] + alignedS2
                (row, col) = (row-1, col-1)
        elif scoreTable[row][col-1] + p == scoreTable[row][col]:
                alignedS1 = "-" + alignedS1
                alignedS2 = s2[col-1:col] + alignedS2
                (row, col) = (row, col-1)
        elif scoreTable[row-1][col-1] + get_score2(s1[row-1], s2[col-1]) == scoreTable[row][col]:
                alignedS1 = s1[row-1:row] + alignedS1
                alignedS2 = s2[col-1:col] + alignedS2
                (row, col) = (row-1, col-1)

    # print(alignedS1)
    # print(alignedS2)
    return

#from scoring matrix get the score of two matching characters
def get_score(letter1):
    pos = inputMatrix[0].index(letter1)
    return int(inputMatrix[pos][pos])

#from scoring matrix get the score of two mismatch characters
def get_score2(letter1, letter2):
    row = inputMatrix[0].index(letter1)
    col = inputMatrix[0].index(letter2)
    return int(inputMatrix[row][col])

#for debugging, print out the DP table in a nice way
def print_grid(grid):
    for row in grid:
        for symbol in row:
            print(str(symbol).rjust(4), end='')
        print("")

#read the txt file with the scoring matrix, conver it into a matrix
def read_matrix(fileName):
    global inputMatrix
    with open(fileName, "r") as input:
        inputMatrix = [[0 for r in range(5)] for j in range(5)]
        for row, line in enumerate(input):
            for col, symbol in enumerate(line.split()):
                inputMatrix[row][col] = symbol


if __name__ == "__main__":
    global s1, s2, scoreTable, p, inputMatrix
    s1 = open(sys.argv[1], "r")
    s1 = s1.readlines()[1:]
    s1 = ''.join(s1).replace('\n', '')
    s2 = open(sys.argv[2], "r")
    s2 = s2.readlines()[1:]
    s2 = ''.join(s2).replace('\n', '')
    p = int(sys.argv[4])
    read_matrix(sys.argv[3])
    traceback()
    # yp with modern: 20778 with scoring matrix saffin
    # ye with modern: 15315 with scoring matrix saffin
