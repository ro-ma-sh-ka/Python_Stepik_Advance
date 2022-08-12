def reverse(digits) -> list:
    if len(digits) <= 1:
        return digits
    return digits[-1] + reverse(digits[1:-1]) + digits[0]


digits = input()
print(reverse(digits))