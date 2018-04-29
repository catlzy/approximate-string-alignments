from __future__ import print_function
import sys
import os

global s1
global s2
global scoreMatrix
global inputMatrix
global p

def create_score_matrix(s1len, s2len):
    global scoreMatrix, p
    scoreMatrix = [[0 for i in range(s2len+1)] for j in range(s1len+1)]

    maxScore = 0
    maxPos = (0,0)
    for i in range(1,s1len+1):
        for j in range(1,s2len+1):
            up = scoreMatrix[i-1][j]+p
            left = scoreMatrix[i][j-1]+p
            if s1[i-1] == s2[j-1]:
                diag = scoreMatrix[i-1][j-1]+get_score(s1[i-1])
            else:
                diag = scoreMatrix[i-1][j-1]+get_score2(s1[i-1], s2[j-1])
            score = max(0, up, left, diag)
            scoreMatrix[i][j] = score
            if score > maxScore:
                maxScore = score
                maxPos = (i,j)
    print("Local alignment score is:" + str(maxScore))
    return maxPos


def traceback():
    global s1, s2, scoreMatrix, p
    alignedS1 = ""
    alignedS2 = ""
    (row, col) = create_score_matrix(len(s1), len(s2))

    while scoreMatrix[row][col] != 0:
        if scoreMatrix[row-1][col] + p == scoreMatrix[row][col]:
            alignedS2 = "-" + alignedS2
            alignedS1 = s1[row-1:row] + alignedS1
            (row,col) = (row-1, col)
        elif s1[row-1] == s2[col-1]:
            if scoreMatrix[row-1][col-1] + get_score(s1[row-1]) == scoreMatrix[row][col]:
                alignedS1 = s1[row-1:row] + alignedS1
                alignedS2 = s2[col-1:col] + alignedS2
                (row, col) = (row-1, col-1)
        elif scoreMatrix[row][col-1] + p == scoreMatrix[row][col]:
                alignedS1 = "-" + alignedS1
                alignedS2 = s2[col-1:col] + alignedS2
                (row, col) = (row, col-1)
        elif scoreMatrix[row-1][col-1] + get_score2(s1[row-1], s2[col-1]) == scoreMatrix[row][col]:
                alignedS1 = s1[row-1:row] + alignedS1
                alignedS2 = s2[col-1:col] + alignedS2
                (row, col) = (row-1, col-1)

    # print(alignedS1)
    # print(alignedS2)
    return


def get_score(letter1):
    pos = inputMatrix[0].index(letter1)
    return int(inputMatrix[pos][pos])


def get_score2(letter1, letter2):
    row = inputMatrix[0].index(letter1)
    col = inputMatrix[0].index(letter2)
    return int(inputMatrix[row][col])


def print_grid(grid):
    for row in grid:
        for symbol in row:
            print(str(symbol).rjust(4), end='')
        print("")

def read_matrix(fileName):
    global inputMatrix, p
    print(fileName)
    with open(fileName, "r") as input:
        inputMatrix = [[0 for r in range(5)] for j in range(5)]
        for row, line in enumerate(input):
            for col, symbol in enumerate(line.split()):
                inputMatrix[row][col] = symbol


if __name__ == "__main__":
    global s1, s2, scoreMatrix, p, inputMatrix
    s1 = open(sys.argv[1], "r")
    s1 = s1.read()
    s2 = open(sys.argv[2], "r")
    s2 = s2.read()
    p = int(sys.argv[4])
    read_matrix(sys.argv[3])
    traceback()
