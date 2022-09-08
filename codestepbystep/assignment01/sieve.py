# https://codestepbystep.com/problem/view/python/collections/set/sieve

def sieve(n: int):
    numbers = [*range(2, n + 1)]          # Asterisk is the "unpacking" operator.
    for i in numbers:
        for j in numbers:
            if j % i == 0 and i != j:
                numbers.remove(j)
    print('Primes:', *numbers, sep = ' ') 

sieve(int(input('Max value N? '))) 

    

