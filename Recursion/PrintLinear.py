def printLinear(n, start = 0):
    if start > n:
        return
    else:
        print(start)
        printLinear(n, start+1)

printLinear(5)

print("******")

def printLinearBackTrack(n):
    if n == 0:
        print(0)
        return
    else:
        printLinearBackTrack(n-1)
        print(n)

printLinearBackTrack(5)