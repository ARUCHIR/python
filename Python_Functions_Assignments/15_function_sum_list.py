# 15. Function to find sum of all elements in a list

def list_sum(numbers):
    total = 0

    for number in numbers:
        total += number

    return total

numbers = [10, 20, 30, 40]
print("Sum:", list_sum(numbers))
