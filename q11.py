decimal_number = float(input("Enter a decimal number: "))

hexadecimal = hex(int(decimal_number))
print(f"Hexadecimal equivalent: {hexadecimal}")

octal = oct(int(decimal_number))
print(f"Octal equivalent: {octal}")

square_root = decimal_number ** 0.5
print(f"Square root: {square_root:.2f}")
