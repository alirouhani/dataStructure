def Merge_Sort_Interval_ASC(x: list):
    l = 1
    n = len(x)
    while l < n:
        g = 0
        m = l
        while m < n:
            d = min(n, m + l)
            s = Fusion(x, g, m, d)
            g = g + 2*l
            m = g + l

        l = 2*l

    return s
            

def Fusion(A: list, g, m, d):
    temp = [0] * d
    for i in range(g, m):
        temp[i] = A[i]
    for j in range(m, d):
        temp[m + d - 1 - j] = A[j]

    i = g
    j = d - 1
    k = g
    while (i < m and j < d):
        if temp[i] <= temp[j]:
            A[k] = temp[i]
            i +=1
            k +=1            
        else:
            A[k] = temp[j]
            j -=1
            k +=1

    return A

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
j=Merge_Sort_Interval_ASC(s)
print(j)
