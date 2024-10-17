#!/usr/bin/python3
def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2

    # Factorize the number and sum up the prime factors
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations