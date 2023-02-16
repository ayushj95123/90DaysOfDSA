def ReverseArray(a, start=0):
    if start == len(a)//2:
        print(a)
    
    else:
        temp = a[start]
        a[start] = a[len(a)-start-1]
        a[len(a)-start-1] = temp
        ReverseArray(a, start+1)

a = [1,2,3,4,5]
ReverseArray(a)
print(a)


