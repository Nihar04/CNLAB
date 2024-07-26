import random

def xor(a, b):
    # Perform XOR operation on two strings
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    # Number of bits to be XORed at a time
    pick = len(divisor)
    
    # Slicing the dividend to get the initial bits
    tmp = dividend[0:pick]
    
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:   # If leftmost bit is '0', use an all-zero divisor
            tmp = xor('0'*pick, tmp) + dividend[pick]
        
        pick += 1
    
    # For the last bit, perform the XOR operation
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    
    return tmp

def encodeData(data, key):
    l_key = len(key)
    
    # Append zeros to the data equal to the length of the key minus 1
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    
    # Append the remainder to the original data
    codeword = data + remainder
    return codeword

def introduceError(data, error_rate=0.1):
    # Introduce errors in the data based on the error rate
    data_list = list(data)
    for i in range(len(data_list)):
        if random.random() < error_rate:
            data_list[i] = '1' if data_list[i] == '0' else '0'
    return ''.join(data_list)

def transmissionWithoutError(data):
    # Simulate transmission without any error
    return data

def transmissionWithError(data, error_rate=0.1):
    # Simulate transmission with errors
    return introduceError(data, error_rate)

# Get user input for data and key
data = input("Enter the data: ")
key = input("Enter the key: ")

print("Original data: ", data)
print("Key: ", key)

encoded_data = encodeData(data, key)
print("Encoded data: ", encoded_data)

# Simulate transmission without error
transmitted_data_without_error = transmissionWithoutError(encoded_data)
print("Transmitted data without error: ", transmitted_data_without_error)

# Simulate transmission with error
transmitted_data_with_error = transmissionWithError(encoded_data)
print("Transmitted data with error: ", transmitted_data_with_error)

