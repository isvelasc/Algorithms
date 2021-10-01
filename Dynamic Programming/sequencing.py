import sys
import numpy as np


def index(x):
    switcher = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
        '-': 4
    }
    return switcher.get(x, None)


def matrix_score(x, y, matrix):
    return matrix[index(y)][index(x)]


def initialize_sequence(x, y, matrix):
    seqMatrix = np.zeros((int(len(x) + 1), int(len(y) + 1)), dtype=list)

    # # initialize matrix
    seqMatrix[0, 0] = 0

    row = 1
    for nuc in x:
        if row == 1:
            seqMatrix[row, 0] = [matrix_score(nuc, '-', matrix), nuc, '-']
            row += 1
            continue

        seqMatrix[row, 0] = [matrix_score(
            nuc, '-', matrix) + seqMatrix[row - 1, 0][0], seqMatrix[row - 1, 0][1] + nuc, seqMatrix[row - 1, 0][2] + '-']
        row += 1

    col = 1
    for nuc in y:
        if col == 1:
            seqMatrix[0, col] = [matrix_score(nuc, '-', matrix), '-', nuc]
            col += 1
            continue

        seqMatrix[0, col] = [matrix_score(
            nuc, '-', matrix) + seqMatrix[0, col - 1][0], seqMatrix[0, col - 1][1] + '-', seqMatrix[0, col - 1][2] + nuc]
        col += 1

    return(seqMatrix)


def maximize_alignment(x, y, matrix, row, col, currSequnce):
    t1 = [matrix_score(x, y, matrix) + currSequnce[row - 1, col - 1][0], currSequnce[row - 1, col - 1][1] + x,
          currSequnce[row - 1, col - 1][2] + y]  # (x,y) -- DP[m-1,n-1]
    t2 = [matrix_score(x, '-', matrix) + currSequnce[row - 1, col][0], currSequnce[row - 1, col][1] + x,
          currSequnce[row - 1, col][2] + '-']  # (x,-) -- DP[m-1,n]
    t3 = [matrix_score('-', y, matrix) + currSequnce[row, col - 1][0], currSequnce[row, col - 1][1] +
          '-', currSequnce[row, col - 1][2] + y]  # (-,y) -- DP[m,n-1]
    if t1[0] == t2[0] == t3[0]:
        return t1
    elif t1[0] > t2[0] and t1[0] > t3[0]:
        return t1
    elif t2[0] > t3[0] and t2[0] > t1[0]:
        return t2
    else:
        return t3


def DNA_seqencing(x, y, matrix):
    seqMatrix = initialize_sequence(x, y, matrix)

    seqMatrix[1, 1] = [matrix_score(x[0], y[0], matrix), x[0], y[0]]

    if len(x) < 2 and len(y) < 2:
        print("x: " + seqMatrix[1, 1][1])
        print("y: " + seqMatrix[1, 1][2])
        print("Score: " + str(seqMatrix[1, 1][0]))
        return

    yloc = 1
    for col in range(2, len(y) + 1):
        seqMatrix[1, col] = maximize_alignment(
            x[0], y[yloc], matrix, 1, col, seqMatrix)
        yloc += 1

    xloc = 1
    yloc = 0
    for row in range(2, len(x) + 1):
        for col in range(1, len(y) + 1):
            seqMatrix[row, col] = maximize_alignment(
                x[xloc], y[yloc], matrix, row, col, seqMatrix)
            yloc += 1
        yloc = 0
        xloc += 1

    print('x:', *seqMatrix[-1, -1][1], sep=" ")
    print('y:', *seqMatrix[-1, -1][2], sep=" ")
    print("Score: " + str(seqMatrix[-1, -1][0]))


def main(argv):
    input = open(argv[1], "r")
    x = input.readline().strip("\n")
    y = input.readline().strip("\n")
    matrix = np.loadtxt(input, skiprows=1, usecols=range(1, 6), dtype=int)
    DNA_seqencing(x, y, matrix)
    input.close()


if __name__ == "__main__":
    main(sys.argv)
