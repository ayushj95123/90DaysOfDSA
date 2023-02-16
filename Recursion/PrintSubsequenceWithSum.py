def PrintSubSequenceWithSum(a, k, index = 0, summ = 0, dp = []):
    
    if index >= len(a):
        if summ == k:
            print(dp)
        return
        #take the current element
    dp.append(a[index])
    PrintSubSequenceWithSum(a, k, index+1, summ+a[index], dp)
        # Dont take current element
    dp.pop()
    PrintSubSequenceWithSum(a, k, index+1, summ, dp)

a = [1,2,3,4,5,0]
PrintSubSequenceWithSum(a, 5)

def PrintAnySubSequenceWithSum(a, k, index = 0, summ = 0, dp = []):
    
    if index >= len(a):
        if summ == k:
            print(dp)
            return True
        return False
    dp.append(a[index])
    if PrintAnySubSequenceWithSum(a, k, index+1, summ+a[index], dp):
        return True
    dp.pop()
    return PrintAnySubSequenceWithSum(a, k, index+1, summ, dp)

b = [1,2,3,4,5,0]
print("*****************")
PrintAnySubSequenceWithSum(b, 5)

def CountSubSequenceWithSum(a, k, index = 0, summ = 0):
    
    if index >= len(a):
        if summ == k:
            return 1
        return 0
    takeCount = CountSubSequenceWithSum(a, k, index+1, summ+a[index])
    dontTakeCount = CountSubSequenceWithSum(a, k, index+1, summ)
    return takeCount + dontTakeCount

c = [1,2,3,4,5]
print("*****************")
print(CountSubSequenceWithSum(c, 5))
