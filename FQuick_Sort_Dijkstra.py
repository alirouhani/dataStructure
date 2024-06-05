def Partition(A: list, g, d):
    p = A[g]
    i = g
    j = g + 1
    h = d
    while j < h:
        if A[j] < p:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i +=1
            j +=1
        elif A[j] > p:
            h = h - 1
            temp = A[h]
            A[h] = A[j]
            A[j] = temp
        else:
            j += 1
    return i, j

def Quick_Sort(A: list, g, d):
    if d - g <= 1:
        return A
    i, j = Partition(A, g, d)
    Quick_Sort(A, g, i)
    Quick_Sort(A, j, d)
    return A
    
s = [92,10,8,83,28,5,21,24,53,43,21,98,65,11,4]
r = Quick_Sort(s, 0, len(s))
print(r)
