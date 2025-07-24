"""
3610. Minimum Number of Primes to Sum to Target
You are given two integers n and m.

You have to select a multiset of prime numbers from the first m prime numbers such that the sum of the selected primes is exactly n. You may use each prime number multiple times.

Return the minimum number of prime numbers needed to sum up to n, or -1 if it is not possible.
"""

def minimumNumberOfPrimes(n: int) -> int:
    # Check for prime using trial division
    def is_prime(x):
        if x < 2:
            return False
        if x == 2 or x == 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False
        i = 5
        while i * i <= x:
            if x % i == 0 or x % (i + 2) == 0:
                return False
            i += 6
        return True

    # Handle base cases
    if n < 2:
        return -1
    if is_prime(n):
        return 1
    if n % 2 == 0:
        return 2  # Even number > 2 is sum of two primes, # Goldbach's conjecture: Every even number greater than 2 can be expressed as the sum of two primes.
    if is_prime(n - 2):
        return 2  # n = 2 + (n - 2), both primes
    return 3  # Otherwise, 3 primes are enough due to number theory





"""
⏱️ Time Complexity:
O(√n) – for the is_prime function (used up to 2 times only)

So, overall time complexity is O(√n)

📦 Space Complexity:
O(1) – constant space"""