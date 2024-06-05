def Partition(A: list, g, d):
    p = A[d]
    i = g
    j = d - 1
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
        temp = A[i + 1]
        A[i + 1] = A[d]
        A[d] = temp
        return i
    else:
        temp = A[i]
        A[i] = A[d]
        A[d] = temp
        return i - 1
    

def Quick_Sort(A: list, g, d):
    if d - g <= 1:
        return A
    while d - g > 1:
        i = Partition(A, g, d)
        Quick_Sort(A, g, i)
        g = i + 1
    return A
    
s = [28,92,10,8,83,5,24,23,35,65,3,54,12,47]
r = Quick_Sort(s, 0, len(s) - 1)
print(r)
