import itertools

def is_prime(x):
    if x == 1 or x == 2 :
        return False
    elif x%2 == 0 :
        return False
    else:
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0 :
                return False
        return True


num_prime = itertools.islice(filter(is_prime, itertools.count(2)), 10000)
print(list(num_prime)[-1])
