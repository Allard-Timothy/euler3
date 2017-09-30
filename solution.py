prime_list = [2]

def prime_generator(min, max):
    if 2 >= min: yield 2
    for i in range(3, max, 2):
        for p in prime_list:
            if i%p == 0 or p*p > i: break
        if i%p:
            prime_list.append(i)
            if i >= min: yield i
        
def factors(n):
    for prime in primes(2, n):
        if n % prime == 0:
            n /= prime
            yield prime
