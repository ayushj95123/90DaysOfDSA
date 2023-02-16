def printReverse(n):
    if n == 0:
        print(0)
        return
    else:
        print(n)
        printReverse(n-1)

printReverse(5)

print("******")


def printReverseBacktrack(n, start = 0):
    if start > n:
        return
    else:
        printReverseBacktrack(n, start+1)
        print(start)

printReverseBacktrack(5) 