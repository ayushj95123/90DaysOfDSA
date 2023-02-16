
#Time complexity 2^n. Exponential
def printFibonacci(n):
    if n <= 1:
        return n

    else:
        return printFibonacci(n-1) + printFibonacci(n-2)

print(printFibonacci(2))
print(printFibonacci(3))
print(printFibonacci(4))
print(printFibonacci(5))

