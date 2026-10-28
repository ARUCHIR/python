# 20. Function to return all prime numbers between two numbers

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def primes_between(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:", primes_between(start, end))
