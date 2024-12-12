#!/usr/bin/python3
def isWinner(x, nums):
    """Determines the winner of each game."""
    
    if not nums or x < 1:
        return None

    # Helper function: Sieve of Eratosthenes
    def sieve(n):
        """Generates a list of booleans indicating prime status up to n."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_num = max(nums)
    prime_status = sieve(max_num)  # Precompute primes
    results = []

    for n in nums:
        primes_left = set(i for i in range(1, n + 1) if prime_status[i])
        turn = 0  # 0 for Maria, 1 for Ben

        while primes_left:
            prime = min(primes_left)
            primes_left -= set(range(prime, n + 1, prime))
            turn = 1 - turn  # Switch turn
        
        # If turn is 0, Ben wins the round, otherwise Maria wins
        results.append("Ben" if turn == 0 else "Maria")

    # Count wins for Maria and Ben
    maria_wins = results.count("Maria")
    ben_wins = results.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
