def binary_to_decimal(binary):
    decimal = 0

    for digit in binary:
        decimal = decimal * 2 + int(digit)

    return decimal


number = input("Enter a binary number: ")

result = binary_to_decimal(number)

print("Decimal value:", result)