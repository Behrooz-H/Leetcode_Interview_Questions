"""
The Dynamic Programming means caching and nothing more tahn that the.
If we have  divides and conquer and there is an repetitive problem. happening aagain and again then it is
an good option for memoization

"""


def fibonacci_memoization(n):
    cache = {}
    def fibo(n: int):
        if n in cache:
            return cache[n]
        elif n == 0:
            cache[0] = 0
            return 0
        elif n == 1 or n == 2:
            cache[0] = 0
            cache[1] = 1
            cache[2] = 1
            return 1
        else:
            cache[n] = fibo(n-1)+fibo(n-2)
            return cache[n]
    print("results", fibo(n))
    print("cache", cache)


if __name__=="__main__":
    print("0")
    fibonacci_memoization(0)
    print("1",fibonacci_memoization(1))
    print("0")
    fibonacci_memoization(0)
    print("2",fibonacci_memoization(2))
    print("3",fibonacci_memoization(3))
    print("4",fibonacci_memoization(4))
    print("5",fibonacci_memoization(5))
    print("10",fibonacci_memoization(10))
    print("12",fibonacci_memoization(12))
    print("15",fibonacci_memoization(15))
    print("20")
    fibonacci_memoization(20)
