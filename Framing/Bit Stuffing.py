def bit_stuffing(binary_data):
    # Define the bit pattern to be stuffed (e.g., '11111')
    pattern = '11111'
    
    # Define the bit to be inserted (usually '0')
    stuffed_bit = '0'
    
    stuffed_data = ''
    count = 0
    
    for bit in binary_data:
        if bit == '1':
            count += 1
        else:
            count = 0
        
        stuffed_data += bit
        
        if count == len(pattern):
            stuffed_data += stuffed_bit
            count = 0
    
    return stuffed_data

def bit_unstuffing(stuffed_data):
    # Define the bit pattern to be unstuffed (e.g., '11111')
    pattern = '11111'
    
    # Define the bit to be removed (usually '0')
    stuffed_bit = '0'
    
    unstuffed_data = ''
    count = 0
    
    i = 0
    while i < len(stuffed_data):
        bit = stuffed_data[i]
        if bit == '1':
            count += 1
        else:
            count = 0
        
        unstuffed_data += bit
        
        if count == len(pattern):
            # Skip the stuffed bit
            i += 1
            count = 0
        
        i += 1
    
    return unstuffed_data

# Example usage
input_data = input("Enter a binary string: ")
stuffed_data = bit_stuffing(input_data)
unstuffed_data = bit_unstuffing(stuffed_data)

print(f"Original data: {input_data}")
print(f"Stuffed data: {stuffed_data}")
print(f"Unstuffed data: {unstuffed_data}")

