def subsetsi( T ):
    
    S = []
    Q = []

    output = []
    i = 0

    while i < len(T):
        for n in range(i,len(T)):
            S.push(n)
            Q.enqueue(S)
            
        i += 1
        while not Q.is_empty():
            temp_stack = Q.dequeue()
            temp = []
            while not temp_stack.is_empty():
                temp.append(temp_stack.pop())

            output.append(temp)

        return output

T = [1,2,3,4,5]
subsetsi(T)
