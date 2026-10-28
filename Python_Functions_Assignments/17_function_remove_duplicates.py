# 17. Function to remove duplicate elements from a list

def remove_duplicates(numbers):
    result = []

    for number in numbers:
        if number not in result:
            result.append(number)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", numbers)
print("Without duplicates:", remove_duplicates(numbers))
