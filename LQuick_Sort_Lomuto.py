def Partition(A: list, g, d):
    p = A[d]
    i = g
    j = g
    while j < d:
        if A[j] <= p:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i +=1
        j +=1
    A[d] = A[i]
    A[i] = p
    return i

def Quick_Sort(A: list, g, d):
    if d - g <= 1:
        return A
    i = Partition(A, g, d)
    Quick_Sort(A, g, i - 1)
    Quick_Sort(A, i, d)
    return A
    
s = [92,10,8,83,28,5,6,34,12,76,36,5,91,38]
r = Quick_Sort(s, 0, len(s) - 1)
print(r)
