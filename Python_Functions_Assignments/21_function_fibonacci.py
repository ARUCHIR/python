# 21. Function to calculate Fibonacci numbers

def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

n = int(input("Enter number of terms: "))
print("Fibonacci series:", fibonacci(n))
