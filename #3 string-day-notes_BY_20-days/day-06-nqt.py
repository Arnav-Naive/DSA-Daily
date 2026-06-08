def fibonacci(n):
    l = []
    for i in range(n):
        if i == 0 or i == 1:
            l.append(i)
        else:
            l.append(l[i-2] + l[i-1])
    return l


print(fibonacci(10))