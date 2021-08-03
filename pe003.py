def pf(n):
    i = 2
    while n >= i :
        if n % i == 0 :
            n //= i
            yield i
        i += 1
        
max(pf(600851475143))
