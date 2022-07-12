binary = int(input("Enter the binary number: "))

decimal = 0
multiplier = 1

while binary > 0:
    last_digit = binary % 10
    decimal = decimal + (last_digit * multiplier)
    multiplier = multiplier * 2
    binary = int(binary/10)

print(f'Decimal value: {decimal}')