# Function to convert Decimal to Binary
def decimal_to_binary(num):
    return bin(num)[2:]

# Function to convert Decimal to Octal
def decimal_to_octal(num):
    return oct(num)[2:]

# Function to convert Decimal to Hexadecimal
def decimal_to_hexadecimal(num):
    return hex(num)[2:].upper()

# Main Program
num = int(input("Enter a decimal number: "))

print("\n----- Number System Conversion -----")
print("Decimal     :", num)
print("Binary      :", decimal_to_binary(num))
print("Octal       :", decimal_to_octal(num))
print("Hexadecimal :", decimal_to_hexadecimal(num))
