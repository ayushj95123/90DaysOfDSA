def printSubsequence(a, index = 0, dp = []):
    if index == len(a):
        print(dp)
    else:
        #Take the current element
        dp.append(a[index])
        printSubsequence(a, index+1, dp)
        dp.pop()
        printSubsequence(a, index+1, dp)

a = [1,2,3]
printSubsequence(a)