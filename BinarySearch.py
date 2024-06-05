def BinarySearch(x: list, a, f , l):
    import math
    m = f + math.floor( (l - f) / 2)
    if x[m]==a:
        return m
    else:
        if x[m] < a:
            f = m
            m=BinarySearch(x, a, f, l)
            return m
        elif (x[m] > a):
            l = m
            m=BinarySearch(x, a, f, l)
            return m

s=[1,5,8,10,15,28,32,40,46,53,63,78,82,91,98,100,103,124,125,137,174,195]
j=BinarySearch(s, 137, 0, len(s)-1)
print(j)
