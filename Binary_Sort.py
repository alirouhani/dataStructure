def Binary_Sort(x: list):
    i = 0
    j = len(x) - 1
    while i <= j:
        if x[i] == 0 or x[j] == 1:
            if x[i] == 0:
                i += 1
            if x[j] == 1:
                j -= 1
        elif x[i] == 1 and x[j] == 0:
            temp = x[i]
            x[i] = x[j]
            x[j] = temp

    return x


s = [0,1,0,0,0,0,0,0,1,1,1,0,1,0]
r = Binary_Sort(s)
print(r)
