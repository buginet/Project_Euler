def gen_fib_even(n):
    a = 1
    b = 2
    while a < n :
        a, b = b, a+b
        if a % 2 == 0 : 
            yield a
            
sum(gen_fib_even(4000000))
