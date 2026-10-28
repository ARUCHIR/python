# 10. Function to check positive, negative or zero

def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

number = int(input("Enter a number: "))
print(check_number(number))
