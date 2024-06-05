def Insertion_Sort(x: list):
    temp = x
    
    for i in range(1, len(temp)):
        j = i - 1
        while temp[j] < temp[j+1] and j >= 0:
            a = temp[j+1]
            temp[j+1] = temp[j]
            temp[j] = a
            j -= 1
    return temp

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
b=Insertion_Sort(s)
print(b)
