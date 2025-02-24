def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence
n = int(input("Enter the number of terms in the Fibonacci sequence: "))
print(f"The first {n} terms of the Fibonacci sequence are:")
print(fibonacci(n))