
def binary_addition(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)

def complement(bin_str):
    return ''.join('1' if bit == '0' else '0' for bit in bin_str)

def calculate_checksum(data):
    if len(data) % 4 != 0:
        data = data.zfill(((len(data) // 4) + 1) * 4)

    chunks = [data[i:i+4] for i in range(0, len(data), 4)]
    checksum = chunks[0]

    for chunk in chunks[1:]:
        checksum = binary_addition(checksum, chunk)

    checksum = binary_addition(checksum, '0' * (4 - len(checksum) % 4))  # Ensure 4-bit length
    checksum = complement(checksum)

    return checksum

def simulate_transmission_with_error(data):
    import random
    data_with_error = list(data)
    error_bit = random.randint(0, len(data_with_error) - 1)
    data_with_error[error_bit] = '1' if data_with_error[error_bit] == '0' else '0'
    print(f"Error introduced at bit position {error_bit}:")
    print(f"Original data: {data}")
    print(f"Data with error: {''.join(data_with_error)}")
    return ''.join(data_with_error)

def receiver(data_with_checksum):
    data = data_with_checksum[:-4]
    received_checksum = data_with_checksum[-4:]

    calculated_checksum = calculate_checksum(data)

    print(f"Received data: {data}")
    print(f"Received checksum: {received_checksum}")
    print(f"Calculated checksum: {calculated_checksum}")

    if calculated_checksum == received_checksum:
        print("No error detected in transmission.")
    else:
        print("Error detected in transmission.")

def main():
    print("Select a scenario:")
    print("1. Transmission with error")
    print("2. Transmission without error")
    choice = input("Enter your choice (1 or 2): ")

    data = input("Enter an 8-bit binary number: ")

    checksum = calculate_checksum(data)
    data_with_checksum = data + checksum

    print(f"Data sent: {data}")
    print(f"Checksum sent: {checksum}")
    print(f"Data with checksum sent: {data_with_checksum}")

    if choice == '1':
        data_with_checksum = simulate_transmission_with_error(data_with_checksum)
    
    receiver(data_with_checksum)

if __name__ == "__main__":
    main()
