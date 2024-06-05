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
    

def Quick_Sort(A: list, g, d):
    if d - g <= 1:
        return A
    while d - g > 1:
        i = Partition(A, g, d)
        Quick_Sort(A, g, i)
        g = i + 1
    return A
    
s = [2,92,10,8,83,5,12,18,29,43,7,56]
r = Quick_Sort(s, 0, len(s) - 1)
print(r)
