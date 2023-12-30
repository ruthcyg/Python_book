import time

# Memoization decorator
def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func

# Recursive lambda function to calculate the Fibonacci sequence with memoization
fibonacci_memoized = memoize(lambda n: n if n <= 1 else fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2))

# Recursive lambda function to calculate the Fibonacci sequence without memoization
fibonacci_non_memoized = lambda n: n if n <= 1 else fibonacci_non_memoized(n - 1) + fibonacci_non_memoized(n - 2)

# Function to measure execution time
def measure_execution_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, end_time - start_time

# Change the value of n for a larger number
n = 30

# Calculate the Fibonacci sequence with memoization
fib_sequence_memoized, time_memoized = measure_execution_time(fibonacci_memoized, n)

# Calculate the Fibonacci sequence without memoization
fib_sequence_non_memoized, time_non_memoized = measure_execution_time(fibonacci_non_memoized, n)

print(f"With memoization: The Fibonacci sequence up to index {n} is: {fib_sequence_memoized}")
print(f"Execution time with memoization: {time_memoized} seconds")

print(f"\nWithout memoization: The Fibonacci sequence up to index {n} is: {fib_sequence_non_memoized}")
print(f"Execution time without memoization: {time_non_memoized} seconds")