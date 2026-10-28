# 11. Function to find maximum of three numbers

def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Maximum:", maximum(10, 30, 20))
