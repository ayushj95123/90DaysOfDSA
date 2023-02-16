def printNTimes(n, str):
    if n == 0:
        return
    else:
        print(str)
        printNTimes(n-1, str)

printNTimes(5, "This is recursion")