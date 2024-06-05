def Selection_Sort_Modified(x: list):
    temp = x
    
    for i in range(len(temp)-1, 0, -1):
        j = 0
        
        while j < i:
            if temp[j] < temp[i]:                
                a = temp[i]
                temp[i] = temp[j]
                temp[j] = a
            j += 1
    return temp

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
b=Selection_Sort_Modified(s)
print(b)
