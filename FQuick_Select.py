def Partition(A: list, g, d):
    p = A[g]
    i = g + 1
    j = d
    while i < j:
        if A[i] <= p or A[j] > p:
            if A[i] <= p:
                i += 1
            if A[j] > p:
                j -= 1
        elif A[i] > p and A[j] < p:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            j -= 1

    if A[i] <= p:
        temp = A[i]
        A[i] = A[g]
        A[g] = temp
        return i
    else:
        temp = A[i - 1]
        A[i - 1] = A[g]
        A[g] = temp
        return i - 1
    

def Quick_Select(A: list, g, d, k):
    if d - g <= 1:
        return A

    if d - g <= 2:
        if d == g + 2 and A[d - 1] < A[g]:
            temp = A[g]
            A[g] = A[d - 1]
            A[d - 1] = temp
            return A[k]
    
    i = Partition(A, g, d)
    if k == i:
        return A[k]
    elif (k < i):
        return Quick_Select(A, g, i, k)
    elif (k > i):
        return Quick_Select(A, i + 1, d,k)
    
s = [28,92,10,8,83,5,24,23,35,65,3,54,12,47]
r = Quick_Select(s, 0, len(s) - 1,5)
print(r)
