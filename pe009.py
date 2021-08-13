for i in range(1,1001):
    c = i
    for x in range(1,500):
        a = x
        b = 1000-(c+x)
        if a**2+b**2==c**2:
            print(a*b*c)
            break
