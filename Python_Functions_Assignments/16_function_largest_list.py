# 16. Function to find largest element in a list

def largest(numbers):
    biggest = numbers[0]

    for number in numbers:
        if number > biggest:
            biggest = number

    return biggest

numbers = [10, 50, 20, 80, 30]
print("Largest:", largest(numbers))
