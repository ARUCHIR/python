# 18. Function to count how many times an element appears in a list

def count_element(numbers, element):
    count = 0

    for number in numbers:
        if number == element:
            count += 1

    return count

numbers = [1, 2, 2, 3, 2, 4]
element = 2

print("Element:", element)
print("Count:", count_element(numbers, element))
