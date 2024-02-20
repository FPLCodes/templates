def check_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True


# Least space
def trial_division(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for prime in primes:
            if prime > int(num**0.5):
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes


# Fastest time
def sieve_of_eratos(n):
    primes = []
    sieve = [True] * (n + 1)
    for x in range(2, int(n**0.5) + 1):
        if sieve[x]:
            for y in range(x * x, n + 1, x):
                sieve[y] = False
    for x in range(2, n + 1):
        if sieve[x]:
            primes.append(x)

    return primes


import heapq


# In between
def dijkstra(n):
    primes_pool = [(4, 2)]
    heapq.heapify(primes_pool)
    primes = [2]
    for i in range(3, n + 1):
        while primes_pool[0][0] < i:
            multiple, prime = heapq.heappop(primes_pool)
            heapq.heappush(primes_pool, (multiple + prime, prime))
        if primes_pool[0][0] == i:
            multiple, prime = heapq.heappop(primes_pool)
            heapq.heappush(primes_pool, (multiple + prime, prime))
        else:
            primes.append(i)
            heapq.heappush(primes_pool, (i * i, i))

    return primes
