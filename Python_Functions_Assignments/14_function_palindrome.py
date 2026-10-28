# 14. Function to check whether a string is a palindrome

def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False

text = input("Enter a string: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
