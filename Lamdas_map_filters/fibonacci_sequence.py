#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones,
# usually starting with 0 and 1.
# The sequence commonly starts as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on.
def fibonacci(n):
    if n<=0:
        return []
    elif n ==1: return [0]
    elif n ==2: return [0,1]
    else :
        fib_sequence = [0,1]
        fib_sequence.extend(map(lambda i: fib_sequence[i-1]+fib_sequence[i-2],range(2,n)))
        return fib_sequence

# Generate the first 10 Fibonacci numbers
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
