def fibonacci(n):
    if n <= 1:   # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(5):   
    print(fibonacci(i))
