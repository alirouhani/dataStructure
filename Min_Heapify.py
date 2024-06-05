def find(value):
    n = len(A)
    for i in range(n):
        if A[i] == value:
            return i
            
def find_child(i: int):
    n = len(A)
    if (2 * i + 1) < n:
        x = A[2 * i + 1]
    else:
        x = 0
    if (2 * i + 2) < n:
        y = A[2 * i + 2]
    else:
        y = 0
    return x, y
        
def Heapify(i: int):
    c1, c2 = find_child(i)
    while c1 + c2 != 0:
        if c1*c2 != 0:
            j = find(min(c1, c2))
        elif (c1 != 0):
            j = find(c1)
        if A[j] < A[i]:
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
        i = j
        c1, c2 = find_child(i)
    return A
                
def Min_Heapify(A: list):
    n = len(A)
    for i in range(n-1, -1, -1):
        A = Heapify(i)
    return A

A=[10,23,14,43,56,86,25,65,12,32,41,38]
B = Min_Heapify(A)
print(B)
        
