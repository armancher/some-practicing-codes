def hex_to_binary(hex_string):
    try:
        # Convert the hexadecimal string to an integer
        decimal_number = int(hex_string, 16)

        # Convert the decimal number to binary representation
        binary_string = bin(decimal_number)[2:]  # [2:] removes the '0b' prefix

        return binary_string
    except ValueError:
        raise ValueError("Invalid hexadecimal string")

# Test the function
if __name__ == "__main__":
    hex_input = input("Enter a hexadecimal number: ")
    try:
        binary_output = hex_to_binary(hex_input)
        print("Binary representation:", binary_output)
    except ValueError as e:
        print("Error:", e)
