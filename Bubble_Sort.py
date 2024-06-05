def Bubble_Sorting(x: list):
    n = len(x)
    temp = x
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if temp[j] < temp[j -1]:
                a = temp[j]
                temp[j] = temp[j -1]
                temp[j-1] = a

    return temp

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
b=Bubble_Sorting(s)
print(b)
