def print_primes(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)

print_primes(100) #prints the prime numbers
