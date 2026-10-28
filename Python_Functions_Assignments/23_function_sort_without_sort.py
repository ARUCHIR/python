# 23. Function to sort a list without using sort()

def sort_list(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

numbers = [5, 2, 8, 1, 3]

print("Original list:", numbers)
print("Sorted list:", sort_list(numbers))
