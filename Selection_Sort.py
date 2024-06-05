def Selection_Sort(x: list):
    temp = x
    
    for i in range(0,len(temp)-1):
        minidx = i
        
        for j in range(i+1, len(temp)):
            if temp[j] > temp[minidx]:                
                minidx = j
                
        if i!=minidx:
            a = temp[i]
            temp[i] = temp[minidx]
            temp[minidx] = a
            
    return temp

s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
b=Selection_Sort(s)
print(b)
