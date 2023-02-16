def sumOfFirstN(n):
    if n == 0:
        return n
    else:
        return n+sumOfFirstN(n-1)


print("Sum of first 5 numbers is",sumOfFirstN(5))


def sumOfFirstNParameterized(n, summ = 0):
    if n == 0:
        print(summ)
    else:
        summ = summ + n
        sumOfFirstNParameterized(n-1, summ)

sumOfFirstNParameterized(5)
    
