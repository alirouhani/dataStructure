def Merge(u: list, v:list, A:list):
    n = len(A)
    if n == 1:
        return A
    
    nu = len(u)
    nv = len(v)
    i = 0
    j = 0
    k = 0
    while (i <= nu-1 and j <= nv-1):
        if u[i] <= v[j]:
            A[k] = u[i]
            i +=1
            k +=1            
        elif u[i] > v[j]:
            A[k] = v[j]
            j +=1
            k +=1
    while i < nu:
        A[k] = u[i]
        i +=1
        k +=1
    while j < nv:
        A[k] = v[j]
        j +=1
        k +=1
        
    return A

def Merge_Sort(x: list):
    import math
    n = len(x)
    temp = x
    m = math.floor(n / 2)
    L = [0] * m
    R = [0] * (n - m)
    if n == 1:
        return temp
    for i in range(m):
        L[i] = temp[i]
    for i in range(n - m):
        R[i] = temp[i + m]

    d = Merge_Sort(L)
    g = Merge_Sort(R)
    s = Merge(d, g, temp)

    return s

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
j=Merge_Sort(s)
print(j)
