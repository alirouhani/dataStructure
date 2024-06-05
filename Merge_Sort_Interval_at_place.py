def Merge_Sort_Interval(x: list, g, d):
    import math
    if d - g < 2:
        return x
    m = math.floor((d+g) / 2)
    u = Merge_Sort_Interval(x, g, m)
    v = Merge_Sort_Interval(x, m, d)
    s = Fusion(x, g, m, d)
    return s

def Fusion(A: list, g, m, d):
    temp = [0] * d
    for i in range(g, d):
        temp[i] = A[i]

    i = g
    j = m
    k = g
    while (i < m and j < d):
        if temp[i] <= temp[j]:
            A[k] = temp[i]
            i +=1
            k +=1            
        else:
            A[k] = temp[j]
            j +=1
            k +=1
    while i < m:
        A[k] = temp[i]
        i +=1
        k +=1
    while j < d:
        A[k] = temp[j]
        j +=1
        k +=1

    return A

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
j=Merge_Sort_Interval(s, 0, len(s))
print(j)
