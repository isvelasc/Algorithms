import sys
from math import floor


def single(A, min, max):
    mid = floor((max + min) / 2)
    mod2 = mid % 2
    if min == max:
        return A[min]
    elif A[mid] == A[mid - 1] and mod2 == 0:
        return single(A, min, mid - 2)
    elif A[mid] == A[mid - 1] and mod2 == 1:
        return single(A, mid + 1, max)
    elif A[mid] == A[mid + 1] and mod2 == 0:
        return single(A, mid + 2, max)
    elif A[mid] == A[mid + 1] and mod2 == 1:
        return single(A, min, mid - 1)
    else:
        return A[mid]


def main(argv):
    input = open(argv[1], "r")
    ls = input.readline().split(', ')
    print(single(ls, 0, len(ls) - 1))
    input.close()


if __name__ == "__main__":
    main(sys.argv)
