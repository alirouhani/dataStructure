def LinearSearch(x: list, a):
    n = len(x)
    for i in range(n):
        if x[i]==a:
            return i

s=[8,"hi",4,"bye"]
j=LinearSearch(s,"bye")
print(j)
