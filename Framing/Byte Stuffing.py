def byte_stuffing(data, flag='f', escape='e'):
    """
    Performs byte stuffing on the input data.
    
    Parameters:
    - data (str): The input data string to be stuffed.
    - flag (str): The flag byte indicating the start/end of the frame.
    - escape (str): The escape byte used for stuffing.
    
    Returns:
    - str: The stuffed data string.
    """
    stuffed_data = flag
    for byte in data:
        if byte == flag or byte == escape:
            stuffed_data += escape
        stuffed_data += byte
    stuffed_data += flag
    return stuffed_data

def byte_unstuffing(stuffed_data, flag='f', escape='e'):
    """
    Performs byte unstuffing on the stuffed data.
    
    Parameters:
    - stuffed_data (str): The stuffed data string to be unstuffed.
    - flag (str): The flag byte indicating the start/end of the frame.
    - escape (str): The escape byte used for unstuffing.
    
    Returns:
    - str: The original unstuffed data string.
    """
    if not (stuffed_data.startswith(flag) and stuffed_data.endswith(flag)):
        raise ValueError("Invalid stuffed data format")
    
    stuffed_data = stuffed_data[1:-1]  # Remove the start and end flags
    unstuffed_data = ''
    escape_next = False
    
    for byte in stuffed_data:
        if escape_next:
            unstuffed_data += byte
            escape_next = False
        elif byte == escape:
            escape_next = True
        else:
            unstuffed_data += byte
    
    return unstuffed_data

def sender():
    """
    Function to handle the sender's operations.
    - Takes user input for the data to be stuffed.
    - Returns the stuffed data.
    """
    data = input("Sender: Enter the string to be stuffed: ")
    stuffed_data = byte_stuffing(data, flag='f', escape='e')
    print(f"Sender: Stuffed Data: {stuffed_data}")
    return stuffed_data

def receiver(stuffed_data):
    """
    Function to handle the receiver's operations.
    - Takes the stuffed data as input.
    - Prints and returns the unstuffed data.
    """
    unstuffed_data = byte_unstuffing(stuffed_data, flag='f', escape='e')
    print(f"Receiver: Unstuffed Data: {unstuffed_data}")
    return unstuffed_data

# Main function to demonstrate sender and receiver
def main():
    stuffed_data = sender()
    unstuffed_data = receiver(stuffed_data)

# Run the main function
if __name__ == "__main__":
    main()

