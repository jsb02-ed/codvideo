def run_length_encode(data):
    # Initialize an empty bytearray
    encoded_data = bytearray()
    # Initialize a counter for consecutive equal bytes
    count = 1

    # Iterate starting from the second byte
    for i in range(1, len(data)):
        # If the current byte is the same as the previous one
        if data[i] == data[i - 1]:
            count += 1
        else:
            # If a different byte is found, append the previous byte and its count
            encoded_data.extend([data[i - 1], count])
            # Reset the count to 1 for the new byte
            count = 1

    # Append the last byte and its count
    encoded_data.extend([data[-1], count])

    # Convert the bytearray to bytes and return the RLE-encoded data
    return bytes(encoded_data)

# Test
input_bytes = b'\x00\x01\x10\xAA\xFF\xFF\x12\x12\x12\x12'
print("input_bytes:", input_bytes)
encoded = run_length_encode(input_bytes)
print("encoded:",encoded)
