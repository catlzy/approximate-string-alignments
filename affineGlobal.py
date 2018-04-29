from __future__ import print_function
import sys
import os

global s1
global s2
global inputMatrix
global H
global V
global D

def create_score_matrix(s1len, s2len):
    global H, V, D, p, a
    inf = float("-inf")
    H = [[inf for i in range(s2len+1)] for j in range(s1len+1)]
    V = [[inf for i in range(s2len+1)] for j in range(s1len+1)]
    D = [[inf for i in range(s2len+1)] for j in range(s1len+1)]
    D[0][0] = 0
    for i in range(s1len+1):
        V[i][0] = p+a*i
    for i in range(s2len+1):
        H[0][i] = p+a*i
    for i in range(1, s1len+1):
        for j in range(1, s2len+1):
            matchScore = get_score2(s1[i-1], s2[j-1])
            D[i][j] = max((D[i-1][j-1]+matchScore), V[i-1][j-1]+matchScore,
                          H[i-1][j-1]+matchScore)
            V[i][j] = max((D[i-1][j]+p+a), (V[i-1][j]+a))
            H[i][j] = max((D[i][j-1]+p+a), (H[i][j-1]+a))
    alignmentScore = max(D[-1][-1], V[-1][-1], H[-1][-1])
    print("Global alignment with affine gap score is:" + str(alignmentScore))
    return alignmentScore


def traceback():
    global H, V, D, s1, s2, p, a
    alignedS1 = ""
    alignedS2 = ""
    score = create_score_matrix(len(s1), len(s2))
    (row, col) = (len(s1), len(s2))
    inH = False
    inV = False
    inD = False
    if D[row][col] == score: inD = True
    elif V[row][col] == score: inV = True
    else: inH = True
    while (row, col) != (0,0):
        if inD == True:
            alignedS1 = s1[row-1:row] + alignedS1
            alignedS2 = s2[col-1:col] + alignedS2
            matchScore = get_score2(s1[row-1], s2[col-1])
            if D[row-1][col-1]+matchScore == score:
                score = D[row-1][col-1]
            elif H[row-1][col-1]+matchScore == score:
                inD = False
                inH = True
                score = H[row-1][col-1]
            elif V[row-1][col-1]+matchScore == score:
                inD = False
                inV = True
                score = V[row-1][col-1]
            (row, col) = (row-1, col-1)
        elif inH == True:
            alignedS1 = "-" + alignedS1
            alignedS2 = s2[col-1:col] + alignedS2
            if D[row][col-1]+p+a == score:
                inH = False
                inD = True
                score = D[row][col-1]
            elif H[row][col-1]+a == score:
                score = H[row][col-1]
            (row, col) = (row, col-1)
        elif inV == True:
            alignedS1 = s1[row-1:row] + alignedS1
            alignedS2 = "-" + alignedS2
            if D[row-1][col]+p+a == score:
                inV = False
                inD = True
                score = D[row-1][col]
            elif V[row-1][col]+a == score:
                score = V[row-1][col]
            (row, col) = (row-1, col)

    print(alignedS1)
    print(alignedS2)

    return


def get_score2(letter1, letter2):
    row = inputMatrix[0].index(letter1)
    col = inputMatrix[0].index(letter2)
    return int(inputMatrix[row][col])


def print_grid(grid):
    for row in grid:
        for symbol in row:
            print(str(symbol).rjust(4), end='    ')
        print("")

def read_matrix(fileName):
    global inputMatrix
    with open(fileName, "r") as input:
        inputMatrix = [[0 for r in range(5)] for j in range(5)]
        for row, line in enumerate(input):
            for col, symbol in enumerate(line.split()):
                inputMatrix[row][col] = symbol


if __name__ == "__main__":
    global s1, s2, scoreMatrix, p, a, inputMatrix
    s1 = open(sys.argv[1], "r")
    s1 = s1.read()
    s2 = open(sys.argv[2], "r")
    s2 = s2.read()
    p = int(sys.argv[4])
    a = float(sys.argv[5])
    read_matrix(sys.argv[3])
    traceback()
