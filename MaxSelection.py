def MaxSelection(x: list, s, n):
    import math
    if n == 1:
        return x[s]
    p = math.floor( n / 2)
    g = MaxSelection(x, s, p)
    d = MaxSelection(x, s + p, n - p)
    if d > g:
        return d
    else:
        return g
    
s=[1,92,10,8,83,5,15,22,12,14,15,76,43,24]
j=MaxSelection(s, 0, len(s))
print(j)
