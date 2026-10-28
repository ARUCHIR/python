# 22. Function to find second-largest number in a list

def second_largest(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    if len(unique_numbers) < 2:
        return None

    largest = unique_numbers[0]
    second = unique_numbers[0]

    for number in unique_numbers:
        if number > largest:
            second = largest
            largest = number
        elif number > second and number != largest:
            second = number

    return second

numbers = [10, 50, 20, 80, 30, 80]
print("Second-largest:", second_largest(numbers))
